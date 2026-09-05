import os as _os
BASE = _os.path.dirname(_os.path.abspath(__file__))
import os
import re
import json

RUNS2 = BASE + "/runs2"
CJK = re.compile(r"[\u4e00-\u9fff]")
LATIN = re.compile(r"[A-Za-z]")
HDR = re.compile(r"^#{1,4}\s*\*{0,2}H([1-6])\b", re.M)


def parse_blocks(text):
    marks = [(m.start(), int(m.group(1))) for m in HDR.finditer(text)]
    res = {}
    for i, (pos, q) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        res.setdefault(q, "")
        res[q] += text[pos:end]
    return res


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


data = {}
report = {}
print(f"{'文件':<12}{'题数':>4}{'思考中文占比':>12}{'思考字符':>9}{'答案字符':>9}")
for fn in sorted(os.listdir(RUNS2)):
    if not fn.endswith(".md"):
        continue
    raw = open(os.path.join(RUNS2, fn), encoding="utf-8").read()
    blocks = parse_blocks(raw)
    data[fn[:-3]] = blocks
    think_all, ans_all = "", ""
    per_q = {}
    for q in range(1, 7):
        sec = split_sections(blocks.get(q, ""))
        t, a = sec.get("【思考】", ""), sec.get("【答案】", "")
        think_all += t
        ans_all += a
        c, l = len(CJK.findall(t)), len(LATIN.findall(t))
        per_q[q] = round(c / (c + l), 3) if (c + l) else None
    c, l = len(CJK.findall(think_all)), len(LATIN.findall(think_all))
    report[fn[:-3]] = {"cjk_ratio": round(c / (c + l), 3) if (c + l) else None,
                       "think_chars": len(think_all), "ans_chars": len(ans_all), "per_q": per_q}
    print(f"{fn[:-3]:<12}{len(blocks):>4}{report[fn[:-3]]['cjk_ratio']:>12}{len(think_all):>9}{len(ans_all):>9}")

json.dump(report, open(BASE + "/manip_check2.json", "w"), ensure_ascii=False, indent=1)

print("\nADAPT 逐题思考语言选择（中文占比）:")
for n in ["ADAPT_H1", "ADAPT_H2", "ADAPT_H3"]:
    print(f"  {n}: " + "  ".join(f"H{q}={report[n]['per_q'][q]}" for q in range(1, 7)))
print("\nNAT 逐题（默认语言）:")
for n in ["NAT_H1", "NAT_H2", "NAT_H3"]:
    print(f"  {n}: " + "  ".join(f"H{q}={report[n]['per_q'][q]}" for q in range(1, 7)))

# aggregate by question
out = []
for q in range(1, 7):
    out.append(f"\n{'='*70}\n## H{q} 的 12 份答案\n{'='*70}")
    for name in sorted(data):
        sec = split_sections(data[name].get(q, ""))
        out.append(f"\n----- {name} -----\n{sec.get('【答案】','').strip() or '(未作答)'}")
open(BASE + "/by_question_hard.md", "w", encoding="utf-8").write("\n".join(out))
print("\n已生成 by_question_hard.md")
