import os as _os
BASE = _os.path.dirname(_os.path.abspath(__file__))
import re
import os
import json
import random
import sys

sys.path.insert(0, BASE + "")
from parser import load_all, split_sections

random.seed(20260905)
BLIND = BASE + "/blind"
os.makedirs(BLIND, exist_ok=True)

data = load_all()
names = sorted(data)
codes = [f"P{i:02d}" for i in range(1, len(names) + 1)]
random.shuffle(codes)
mapping = {}
hint_re = re.compile(r"(思考|推理)过程(我)?(用|使用|选择)了?[^。\n]{0,10}(英文|中文|英语|汉语)[^。\n]{0,15}。?")

for code, name in zip(codes, names):
    mapping[code] = name
    lines = [f"# 答卷 {code}", ""]
    for q in range(1, 11):
        sec = split_sections(data[name][q])
        ans = sec.get("【答案】", "").strip()
        ans = hint_re.sub("", ans)
        if not ans:
            ans = "(未作答)"
        lines.append(f"## Q{q}")
        lines.append(ans)
        lines.append("")
    open(os.path.join(BLIND, f"{code}.md"), "w", encoding="utf-8").write("\n".join(lines))

json.dump(mapping, open(os.path.join(BLIND, "_key.json"), "w"), ensure_ascii=False, indent=1)
print("匿名化完成:", len(codes), "份")
for c in codes:
    p = os.path.join(BLIND, f"{c}.md")
    txt = open(p, encoding="utf-8").read()
    ok = txt.count("## Q") == 10 and "(未作答)" not in txt
    print(f"  {c} -> {mapping[c]:<10} 题数={txt.count('## Q'):2d} 完整={ok} 字符={len(txt)}")
