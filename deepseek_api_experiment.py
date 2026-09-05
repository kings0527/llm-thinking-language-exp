"""DeepSeek 思考语言实验：直接调用 DeepSeek API 测试思考语言对质量/成本的影响。

用法：
  export DEEPSEEK_API_KEY=sk-xxxx
  python3 deepseek_api_experiment.py --models deepseek-reasoner --conds EN,ZH,NAT --rounds 3 --questions H1,H2,H3,H4,H5,H6
  python3 deepseek_api_experiment.py --dry-run   # 只打印计划，不调用

说明：
- deepseek-reasoner（R1）的原生思维链在响应的 reasoning_content 字段，脚本会保存并统计思考语言占比（操纵检验）
- deepseek-chat（V3）无原生思维链，用"先写推理再作答"的外显方式近似
- 每次调用的 usage（prompt/completion/reasoning tokens）全部记录，成本按官方定价折算
- 结果逐条落盘 results_deepseek/，支持断点续跑（已存在的结果自动跳过）
- 答卷可直接用 score_auto.py 的机械评分器评分（对【答案】段或 content 字段）
"""
import argparse
import json
import os
import re
import time
import urllib.request
import urllib.error

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "results_deepseek")
API_URL = "https://api.deepseek.com/chat/completions"

# 官方定价（元 / 百万 token），如涨价请在此更新
PRICE = {
    "deepseek-reasoner": {"in": 4.0, "out": 16.0},
    "deepseek-chat": {"in": 2.0, "out": 8.0},
}

COND_INSTR = {
    "EN": {
        "zh": "请严格用英文逐步推理（推理过程全英文），最终答案用简体中文给出。",
        "en": "Think through this step by step in English (reasoning entirely in English), then give the final answer in Simplified Chinese.",
    },
    "ZH": {
        "zh": "请严格用中文逐步推理（推理过程全中文），最终答案用简体中文给出。",
        "en": "Think through this step by step in Chinese (reasoning entirely in Chinese), then give the final answer in Simplified Chinese.",
    },
    "NAT": {
        "zh": "请用你觉得最自然的语言逐步推理，最终答案用简体中文给出。",
        "en": "Reason in whichever language feels most natural, then give the final answer in Simplified Chinese.",
    },
}


def load_questions(wanted):
    """从 hard_questions.md 按 **H1**...**H6** 拆题"""
    src = open(os.path.join(BASE, "hard_questions.md"), encoding="utf-8").read()
    parts = re.split(r"\*\*(H(\d)[^*]*)\*\*", src)
    q = {}
    for i in range(1, len(parts), 3):
        num = int(parts[i + 1])
        body = (parts[i] + parts[i + 2]).strip()
        q[num] = f"**{parts[i]}**{parts[i + 2]}"
    return {k: v for k, v in q.items() if k in wanted}


CJK = re.compile(r"[\u4e00-\u9fff]")
LATIN = re.compile(r"[A-Za-z]")


def lang_ratio(text):
    c, l = len(CJK.findall(text)), len(LATIN.findall(text))
    tot = c + l
    return round(c / tot, 3) if tot else None


def call_api(key, model, messages, max_retries=4):
    payload = json.dumps({"model": model, "messages": messages, "stream": False}).encode()
    req = urllib.request.Request(
        API_URL, data=payload,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {key}"},
    )
    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(req, timeout=600) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503) and attempt < max_retries - 1:
                time.sleep(2 ** attempt * 2)
                continue
            raise
    raise RuntimeError("unreachable")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", default="deepseek-reasoner")
    ap.add_argument("--conds", default="EN,ZH,NAT")
    ap.add_argument("--rounds", type=int, default=3)
    ap.add_argument("--questions", default="H1,H2,H3,H4,H5,H6")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    key = os.environ.get("DEEPSEEK_API_KEY")
    if not key and not args.dry_run:
        raise SystemExit("请先 export DEEPSEEK_API_KEY=sk-xxx")

    models = args.models.split(",")
    conds = args.conds.split(",")
    qids = [int(x.replace("H", "")) for x in args.questions.split(",")]
    questions = load_questions(qids)
    os.makedirs(OUT, exist_ok=True)

    plan = []
    for model in models:
        for cond in conds:
            for r in range(1, args.rounds + 1):
                for qid in qids:
                    fn = os.path.join(OUT, f"{model}_{cond}_R{r}_H{qid}.json")
                    if os.path.exists(fn):
                        continue
                    plan.append((model, cond, r, qid, fn))

    n_calls = len(plan)
    est_out = 4000 if any("reasoner" in m for m in models) else 1500
    est_cost = n_calls * (500 * 4.0 + est_out * 16.0) / 1e6
    print(f"计划调用 {n_calls} 次；预估成本 ≈ ¥{est_cost:.2f}（按 reasoner 输出 {est_out} tok/次粗估）")
    if args.dry_run:
        for m, c, r, q, f in plan[:8]:
            print(f"  {m} {c} R{r} H{q}")
        print("  ...（--dry-run 不实际调用）")
        return

    for i, (model, cond, r, qid, fn) in enumerate(plan, 1):
        instr = COND_INSTR[cond]["zh"]
        messages = [{"role": "user", "content": f"{instr}\n\n{questions[qid]}"}]
        t0 = time.time()
        try:
            resp = call_api(key, model, messages)
        except Exception as e:
            print(f"[{i}/{n_calls}] {model} {cond} R{r} H{qid} FAILED: {e}")
            continue
        dt = time.time() - t0
        choice = resp["choices"][0]
        reasoning = choice["message"].get("reasoning_content") or ""
        content = choice["message"]["content"]
        usage = resp.get("usage", {})
        det = usage.get("completion_tokens_details") or {}
        price = PRICE.get(model)
        rec = {
            "model": model, "cond": cond, "round": r, "question": f"H{qid}",
            "reasoning_content": reasoning,
            "reasoning_lang_cjk_ratio": lang_ratio(reasoning),
            "content": content,
            "usage": usage,
            "reasoning_tokens": det.get("reasoning_tokens"),
            "cost_cny": (None if price is None else
                         (usage.get("prompt_tokens", 0) * price["in"]
                          + usage.get("completion_tokens", 0) * price["out"]) / 1e6),
            "latency_s": round(dt, 1),
        }
        json.dump(rec, open(fn, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        cost_s = f"¥{rec['cost_cny']:.4f}" if rec["cost_cny"] is not None else "¥?(未录该模型定价)"
        print(f"[{i}/{n_calls}] {model} {cond} R{r} H{qid}  "
              f"out={usage.get('completion_tokens','?')}tok(思考{rec['reasoning_tokens'] or 0}) "
              f"思考中文占比={rec['reasoning_lang_cjk_ratio']}  {cost_s}  {dt:.0f}s")

    # 汇总
    rows = []
    for f in sorted(os.listdir(OUT)):
        if f.endswith(".json"):
            rows.append(json.load(open(os.path.join(OUT, f), encoding="utf-8")))
    if rows:
        print(f"\n===== 汇总（{len(rows)} 条）=====")
        import collections
        agg = collections.defaultdict(lambda: {"tok": 0, "cjk": [], "n": 0, "cost": 0.0})
        for x in rows:
            k = (x["model"], x["cond"])
            a = agg[k]
            a["tok"] += (x["usage"].get("completion_tokens") or 0)
            a["cost"] += x["cost_cny"] or 0.0
            a["n"] += 1
            if x["reasoning_lang_cjk_ratio"] is not None:
                a["cjk"].append(x["reasoning_lang_cjk_ratio"])
        for (m, c), a in sorted(agg.items()):
            avg_cjk = sum(a["cjk"]) / len(a["cjk"]) if a["cjk"] else float("nan")
            print(f"{m:<20}{c:<5} n={a['n']:<3} 输出合计={a['tok']:>7}tok  "
                  f"思考中文占比均值={avg_cjk:.2f}  成本合计=¥{a['cost']:.2f}")


if __name__ == "__main__":
    main()
