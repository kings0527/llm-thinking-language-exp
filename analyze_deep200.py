import os as _os
BASE = _os.path.dirname(_os.path.abspath(__file__))
import os
import re
import json

BASE = BASE
G = json.load(open(os.path.join(BASE, "deep_gold_200.json")))
STEPS, FINAL = G["steps"], G["final"]
RUNS3 = os.path.join(BASE, "runs3")
PAT = re.compile(r"(?:第\s*(\d+)\s*步后?|Step\s*(\d+))\s*[=＝:：]\s*(-?\d+)")

print(f"金标准最终值 = {FINAL}\n")
print(f"{'运行':<16}{'报告步数':>8}{'首次出错':>9}{'错误步数':>9}{'逐步正确率':>10}{'终值':>10}{'终值正确':>8}")
out = {}
for fn in sorted(os.listdir(RUNS3)):
    if "200" not in fn or not fn.endswith(".md"):
        continue
    raw = open(os.path.join(RUNS3, fn), encoding="utf-8").read()
    parts = raw.split("【答案】")
    ans = parts[1] if len(parts) > 1 else raw
    vals = {}
    for m in PAT.finditer(ans):
        k = int(m.group(1) or m.group(2))
        if 1 <= k <= 200 and k not in vals:
            vals[k] = int(m.group(3))
    first_err, n_wrong = None, 0
    for k in range(1, 201):
        if k in vals and vals[k] != STEPS[k - 1]:
            n_wrong += 1
            if first_err is None:
                first_err = k
    fm = re.search(r"最终结果\s*[=＝:：]?\s*(-?\d+)", ans)
    fv = int(fm.group(1)) if fm else vals.get(200)
    name = fn[:-3]
    out[name] = {"reported": len(vals), "first_error": first_err, "wrong": n_wrong,
                 "acc": round((200 - n_wrong) / 200, 3), "final": fv, "ok": fv == FINAL}
    fe = first_err if first_err else "-"
    print(f"{name:<16}{len(vals):>8}{str(fe):>9}{n_wrong:>9}{out[name]['acc']*100:>9.1f}%{str(fv):>10}{'✓' if fv == FINAL else '✗':>8}")

json.dump(out, open(os.path.join(BASE, "deep200_results.json"), "w"), ensure_ascii=False, indent=1)
