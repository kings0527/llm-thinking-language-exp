import os as _os
BASE = _os.path.dirname(_os.path.abspath(__file__))
import re
import json
import sys

sys.path.insert(0, BASE + "")
from parser import load_all, split_sections

CJK = re.compile(r"[\u4e00-\u9fff]")
LATIN = re.compile(r"[A-Za-z]")

data = load_all()
report = {}
print(f"{'文件':<12}{'题数':>4}{'思考中文占比':>12}{'思考字符数':>10}{'答案字符数':>10}")
for name, blocks in data.items():
    assert len(blocks) == 10, f"{name} 只解析出 {len(blocks)} 题"
    think_all, ans_all = "", ""
    per_q = {}
    for q in range(1, 11):
        sec = split_sections(blocks[q])
        t = sec.get("【思考】", "")
        a = sec.get("【答案】", "")
        think_all += t
        ans_all += a
        c, l = len(CJK.findall(t)), len(LATIN.findall(t))
        tot = c + l
        per_q[q] = round(c / tot, 3) if tot else None
    c, l = len(CJK.findall(think_all)), len(LATIN.findall(think_all))
    ratio = round(c / (c + l), 3) if (c + l) else None
    report[name] = {"cjk_ratio": ratio, "think_chars": len(think_all), "ans_chars": len(ans_all), "per_q": per_q}
    print(f"{name:<12}{len(blocks):>4}{ratio:>12}{len(think_all):>10}{len(ans_all):>10}")

json.dump(report, open(BASE + "/manipulation_check.json", "w"), ensure_ascii=False, indent=1)

print("\n每题思考语言（中文字符占比，仅 ADAPT 与 EN 列出）：")
for name in ["ADAPT_R1", "ADAPT_R2", "ADAPT_R3", "EN_R1", "NAT_R1", "ZH_R1"]:
    print(f"  {name}: " + " ".join(f"Q{q}={report[name]['per_q'][q]}" for q in range(1, 11)))
