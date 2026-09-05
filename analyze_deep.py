import os as _os
BASE = _os.path.dirname(_os.path.abspath(__file__))
import os
import re
import json

BASE = BASE
GOLD = json.load(open(os.path.join(BASE, "deep_gold.json")))["50"]
STEPS = GOLD["steps"]
FINAL = GOLD["final"]
RUNS3 = os.path.join(BASE, "runs3")

PAT = re.compile(r"第\s*(\d+)\s*步后?\s*[=＝:：]\s*(-?\d+)")


def analyze(fn):
    raw = open(os.path.join(RUNS3, fn), encoding="utf-8").read()
    # 只取【答案】段
    parts = raw.split("【答案】")
    ans = parts[1] if len(parts) > 1 else raw
    vals = {}
    for m in PAT.finditer(ans):
        k = int(m.group(1))
        if 1 <= k <= 50 and k not in vals:
            vals[k] = int(m.group(2))
    if not vals:
        return None
    # 第一次出错步
    first_err = None
    n_wrong = 0
    for k in range(1, 51):
        if k in vals and vals[k] != STEPS[k - 1]:
            n_wrong += 1
            if first_err is None:
                first_err = k
    final_m = re.search(r"最终结果\s*[=＝:：]?\s*(-?\d+)", ans)
    final_val = int(final_m.group(1)) if final_m else (vals.get(50) if 50 in vals else None)
    return {
        "steps_reported": len(vals),
        "first_error_step": first_err,
        "n_wrong_steps": n_wrong,
        "step_acc": round(50 - n_wrong) / 50,
        "final_correct": final_val == FINAL,
        "final_val": final_val,
        "gold_final": FINAL,
    }


print(f"金标准最终值 = {FINAL}\n")
print(f"{'运行':<16}{'报告步数':>8}{'首次出错':>9}{'错误步数':>9}{'逐步正确率':>10}{'最终值':>10}{'终值正确':>9}")
rows = {}
for fn in sorted(os.listdir(RUNS3)):
    if not fn.endswith(".md"):
        continue
    r = analyze(fn)
    rows[fn[:-3]] = r
    if r is None:
        print(f"{fn:-<16}  无法解析")
        continue
    fe = r["first_error_step"] if r["first_error_step"] else "-"
    fv = r["final_val"] if r["final_val"] is not None else "?"
    print(f"{fn[:-3]:<16}{r['steps_reported']:>8}{str(fe):>9}{r['n_wrong_steps']:>9}"
          f"{r['step_acc']*100:>9.0f}%{str(fv):>10}{'✓' if r['final_correct'] else '✗':>9}")

json.dump(rows, open(os.path.join(BASE, "deep_pilot_results.json"), "w"), ensure_ascii=False, indent=1)
