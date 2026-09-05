import os as _os
BASE = _os.path.dirname(_os.path.abspath(__file__))
import json
import os
import re
import sys

sys.path.insert(0, BASE + "")
from parser import load_all, split_sections

data = load_all()
out = []
for q in range(1, 11):
    out.append(f"\n{'='*70}\n## Q{q} 的 12 份答案（按条件×轮次）\n{'='*70}")
    for name in sorted(data):
        sec = split_sections(data[name][q])
        ans = sec.get("【答案】", "").strip()
        out.append(f"\n----- {name} -----\n{ans}")
open(BASE + "/by_question_all.md", "w", encoding="utf-8").write("\n".join(out))

# mechanical check of objective questions
print("=== Q1 客观核对（金标准 = 6）===")
for name in sorted(data):
    a = split_sections(data[name][1]).get("【答案】", "")
    # find the final numeric claim
    nums = re.findall(r"a[₂2][₀0][₂2][₆6]\s*(?:=|＝|是|为)\s*\*{0,2}(\d+)", a)
    print(f"  {name:<10} 抓到最终数值: {nums if nums else 'N/A'}")

print("\n=== Q2 客观核对（金标准: 丁1 丙2 戊3 乙4 甲5）===")
GOLD = {"丁": 1, "丙": 2, "戊": 3, "乙": 4, "甲": 5}
for name in sorted(data):
    a = split_sections(data[name][2]).get("【答案】", "")
    found = {}
    for m in re.finditer(r"([甲乙丙丁戊])[^\d\n]{0,6}第?\s*\*{0,2}([1-5１-５])", a):
        ch, n = m.group(1), int(m.group(2))
        found.setdefault(ch, n)
    ok = all(found.get(k) == v for k, v in GOLD.items()) and len(found) >= 5
    print(f"  {name:<10} {found}  {'✅ 全对' if ok else '❌'}")

print("\n=== Q10 客观核对（金标准 = 7 个 1/4 杯 + 2 汤匙）===")
for name in sorted(data):
    a = split_sections(data[name][10]).get("【答案】", "")
    qc = re.findall(r"(\d+)\s*(?:次|个)?\s*\*{0,2}1/4\s*杯", a)
    tb = re.findall(r"(\d+)\s*(?:汤匙|匙|tablespoons?)", a)
    print(f"  {name:<10} 1/4杯次数={qc[:4]} 汤匙={tb[:4]}")
