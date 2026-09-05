import os as _os
BASE = _os.path.dirname(_os.path.abspath(__file__))
import os
import re
import json
import sys

sys.path.insert(0, BASE + "")
import tiktoken
from scores import SCORES, DETAIL_R2

ENC = tiktoken.get_encoding("cl100k_base")
BASE = BASE
CJK = re.compile(r"[\u4e00-\u9fff]")
CONDS = ["EN", "ZH", "NAT", "ADAPT"]


def split_sections(text):
    parts = re.split(r"(【思考】|【答案】|【判断题型】)", text)
    out, cur = {}, None
    for p in parts:
        if p in ("【思考】", "【答案】", "【判断题型】"):
            cur = p
            out.setdefault(cur, "")
        elif cur:
            out[cur] += p
    return out


def blocks_for(d, pat):
    HDR = re.compile(pat, re.M)
    res = {}
    for fn in sorted(f for f in os.listdir(d) if f.endswith(".md")):
        raw = open(os.path.join(d, fn), encoding="utf-8").read()
        marks = [(m.start(), int(m.group(1))) for m in HDR.finditer(raw)]
        b = {}
        for i, (pos, q) in enumerate(marks):
            end = marks[i + 1][0] if i + 1 < len(marks) else len(raw)
            b.setdefault(q, "")
            b[q] += raw[pos:end]
        res[fn[:-3]] = b
    return res


def stats(d, pat, nq):
    rows = {}
    for name, b in blocks_for(d, pat).items():
        think, ans = "", ""
        for q in range(1, nq + 1):
            sec = split_sections(b.get(q, ""))
            think += sec.get("【思考】", "")
            ans += sec.get("【答案】", "")
        rows[name] = {
            "think_tok": len(ENC.encode(think)),
            "ans_tok": len(ENC.encode(ans)),
            "think_chars": len(think),
            "cjk_ratio": round(len(CJK.findall(think)) / max(len(think), 1), 3),
        }
    return rows


r1 = stats(os.path.join(BASE, "runs"), r"^#{1,4}\s*\*{0,2}Q(\d+)", 10)
r2 = stats(os.path.join(BASE, "runs2"), r"^#{1,4}\s*\*{0,2}H([1-6])\b", 6)
json.dump({"round1": r1, "round2": r2}, open(os.path.join(BASE, "token_stats.json"), "w"), ensure_ascii=False, indent=1)


def report(rows, title, maxscore, sc):
    print(f"\n{'='*78}\n{title}（满分 {maxscore}）\n{'='*78}")
    print(f"{'条件':<7}{'思考tok':>9}{'答案tok':>9}{'合计tok':>9}{'思考字符':>9}{'中文占比':>9}{'得分':>7}{'tok/分':>9}")
    out = {}
    for cond in CONDS:
        names = [n for n in rows if n.startswith(cond + "_")]
        tt = sum(rows[n]["think_tok"] for n in names) / len(names)
        at = sum(rows[n]["ans_tok"] for n in names) / len(names)
        tc = sum(rows[n]["think_chars"] for n in names) / len(names)
        cr = sum(rows[n]["cjk_ratio"] for n in names) / len(names)
        avg = sum(sc[n] for n in names) / len(names)
        out[cond] = {"think_tok": tt, "ans_tok": at, "chars": tc, "cjk": cr, "score": avg, "tok_per_pt": tt / avg}
        print(f"{cond:<7}{tt:>9.0f}{at:>9.0f}{tt+at:>9.0f}{tc:>9.0f}{cr:>9.3f}{avg:>7.2f}{tt/avg:>9.0f}")
    base = out["ZH"]["think_tok"]
    print("  相对中文思考的 token 倍数: " + "  ".join(f"{c}={out[c]['think_tok']/base:.2f}x" for c in CONDS))
    return out


o1 = report(r1, "第一轮（中等难度 10 题）", 20, SCORES["第一轮"])
o2 = report(r2, "第二轮（高难度 6 题）", 12, SCORES["第二轮"])

print(f"\n{'='*78}\n第二轮 按题型的语言选择 vs 得分（H=中文强依赖, E=英文强依赖, N=语言中性）\n{'='*78}")
QT = {1: "H 古汉语", 2: "N 组合计数", 3: "E 英语语用", 4: "N 逻辑", 5: "H 汉语歧义", 6: "E 英语搭配"}
print(f"{'题':<12}" + "".join(f"{c:>8}" for c in CONDS))
for q in range(1, 7):
    row = []
    for c in CONDS:
        ns = [n for n in DETAIL_R2 if n.startswith(c + "_")]
        row.append(sum(DETAIL_R2[n][q - 1] for n in ns) / len(ns))
    print(f"{QT[q]:<12}" + "".join(f"{v:>8.2f}" for v in row))

print("\n【核心结论】两轮合计：")
tot = {}
for c in CONDS:
    tt = o1[c]["think_tok"] + o2[c]["think_tok"]
    at = o1[c]["ans_tok"] + o2[c]["ans_tok"]
    ss = o1[c]["score"] + o2[c]["score"]
    tot[c] = {"think": tt, "ans": at, "score": ss, "per_pt": tt / ss}
for c in CONDS:
    t = tot[c]
    print(f"  {c:<7} 思考token={t['think']:>7.0f}  答案token={t['ans']:>7.0f}  总得分={t['score']:>6.2f}/32  "
          f"每分思考成本={t['per_pt']:>6.0f} tok  (相对ZH={t['per_pt']/tot['ZH']['per_pt']:.2f}x)")

print("\n【语义详尽度 vs token 成本】")
for c in CONDS:
    ch1, ch2 = o1[c]["chars"], o2[c]["chars"]
    print(f"  {c:<7} 思考字符={ch1+ch2:>7.0f}  思考token={tot[c]['think']:>7.0f}  "
          f"字符/token={(ch1+ch2)/tot[c]['think']:>5.2f}")
