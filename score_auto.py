import os as _os
BASE = _os.path.dirname(_os.path.abspath(__file__))
"""20 轮扩展实验的全自动评分：
- H2/H4：客观题严格 0/2
- H6：6 小句机械核对（meeting / suggested-that-taking / despite-or-in-spite / capable-of / than+go / worth-trying）
- H1：三点关键词核对（旁指义 / 后起演变 / 误读偏差）
- H3：三点核对（命题相同+立场 / 预设应然 / 反例说明）
- H5：立场分类（c: 否定句歧义是否更强）——分类结果供人工复核
输出 scores_auto.json + h5_stances.json（含原文供复核）
"""
import os
import re
import json

BASE = BASE
RUNS2 = os.path.join(BASE, "runs2")
HDR = re.compile(r"^#{1,4}\s*\*{0,2}H([1-6])\b", re.M)


def parse_blocks(text):
    marks = [(m.start(), int(m.group(1))) for m in HDR.finditer(text)]
    b = {}
    for i, (pos, q) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        b.setdefault(q, "")
        b[q] += text[pos:end]
    return b


def answer_of(block):
    parts = block.split("【答案】")
    return (parts[1] if len(parts) > 1 else "").strip()


scores = {}
h5 = {}
h_flags = {}
for fn in sorted(os.listdir(RUNS2)):
    if not fn.endswith(".md"):
        continue
    name = fn[:-3]
    if not re.match(r"^(EN|ZH)_H\d+$", name):
        continue
    blocks = parse_blocks(open(os.path.join(RUNS2, fn), encoding="utf-8").read())
    s = {}

    # H2 客观：576
    a2 = answer_of(blocks.get(2, ""))
    s["H2"] = 2 if re.search(r"576", a2) else 0

    # H4 客观：A无赖 B骑士 C无赖
    a4 = answer_of(blocks.get(4, ""))
    t = []
    for who in ["A", "B", "C"]:
        m = re.search(who + r"[^\n]{0,12}?(骑士|无赖)", a4)
        t.append(m.group(1) if m else "?")
    s["H4"] = 2 if t == ["无赖", "骑士", "无赖"] else 0

    # H6 六句机械核对
    a6 = answer_of(blocks.get(6, ""))
    checks = {
        1: bool(re.search(r"forward to\s+(meeting|seeing)", a6, re.I)) or bool(re.search(r"to meet(ing)? you", a6, re.I)) and bool(re.search(r"meeting", a6, re.I)),
        2: bool(re.search(r"suggested\s+(that\s+(I|he|she)|taking|my taking)", a6, re.I)),
        3: bool(re.search(r"(Despite the rain(?! of)|In spite of the rain)", a6, re.I)) and not bool(re.search(r"Despite of", a6, re.I)),
        4: bool(re.search(r"capable of", a6, re.I)),
        5: bool(re.search(r"than (go\b|stay)", a6, re.I)) and not bool(re.search(r"than to go", a6, re.I)),
        6: bool(re.search(r"worth (trying|a try)", a6, re.I)) and not bool(re.search(r"worth to try", a6, re.I)),
    }
    ok6 = sum(checks.values())
    s["H6"] = 2 if ok6 == 6 else (1 if ok6 >= 4 else 0)
    if ok6 < 6:
        h_flags.setdefault(name, []).append(f"H6 {ok6}/6 " + ",".join(str(k) for k, v in checks.items() if not v))

    # H1 三点关键词
    a1 = answer_of(blocks.get(1, ""))
    k1 = {
        "旁指": bool(re.search(r"(别的|其他的|其它|其他的事|别的事|other|其余)", a1)),
        "后起": bool(re.search(r"(后起|后世|中古|魏晋|唐|汉以|先秦.{0,12}(没有|尚未|无)|不是第三人称|不作人称|没有.{0,8}第三人称|later|not.{0,20}pronoun|grammaticaliz|emerged)", a1, re.I)),
        "偏差": bool(re.search(r"(偏差|丢失|失去|误读|凭空|变成|错解|歪曲|歧义|转移话题|岔开|avoid|lose|shift|distort)", a1, re.I)),
    }
    s["H1"] = 2 if all(k1.values()) else (1 if sum(k1.values()) == 2 else 0)
    if s["H1"] < 2:
        h_flags.setdefault(name, []).append("H1 miss:" + ",".join(k for k, v in k1.items() if not v))

    # H3 三点
    a3 = answer_of(blocks.get(3, ""))
    k3 = {
        "立场": bool(re.search(r"(批评|责备|责怪|不满|负面|怠慢|轻|不以为然|嫌|lazy|critic|blame|disapprove|negative|reproach)", a3, re.I)),
        "预设应然": bool(re.search(r"(本应|本该|理应|应该|应当|期待|预期|理所当然|轻而易举|举手之劳|expected|supposed|norm|ought|entail)", a3, re.I)),
        "反例": bool(re.search(r"(不能|不适合|不自然|无法|不能用来|odd|unnatural|inappropriate|cannot|fail)", a3, re.I)),
    }
    s["H3"] = 2 if all(k3.values()) else (1 if sum(k3.values()) == 2 else 0)
    if s["H3"] < 2:
        h_flags.setdefault(name, []).append("H3 miss:" + ",".join(k for k, v in k3.items() if not v))

    # H5 立场分类（供人工复核）
    a5 = answer_of(blocks.get(5, ""))
    same = bool(re.search(r"(歧义程度)?(基本|完全)?相?同|两种理解都|同样存在歧义|歧义相当|一样", a5))
    diff = bool(re.search(r"(歧义程度)?(不|并)?(完全)?相同|更弱|更低|更强|只有一种|几乎只有|不明显|更弱|较弱|不对称|更低|不同", a5))
    stronger_neg = bool(re.search(r"(否定句|“他谁都不认识”|他谁都不认识).{0,40}(更强|更实|更均衡|更自然|更突出)", a5))
    weaker_pos = bool(re.search(r"(他谁都认识).{0,40}(更弱|较弱|低|只有|倾向|占优|主导)", a5))
    stance = "DIFF" if (diff or stronger_neg or weaker_pos) and not (same and not (stronger_neg or weaker_pos)) else "SAME"
    # 更细：同时出现相同与不同表述时以具体判断为准
    if weaker_pos or stronger_neg:
        stance = "DIFF"
    h5[name] = {"stance": stance, "text": a5[:600]}
    s["H5"] = 2 if stance == "DIFF" else 1

    scores[name] = s

json.dump(scores, open(os.path.join(BASE, "scores_auto.json"), "w"), ensure_ascii=False, indent=1)
json.dump(h5, open(os.path.join(BASE, "h5_stances.json"), "w"), ensure_ascii=False, indent=1)

# 汇总
import collections
print(f"{'样本':<12}{'H1':>3}{'H2':>3}{'H3':>3}{'H4':>3}{'H5':>3}{'H6':>3}{'合计':>4}")
totals = collections.defaultdict(list)
for name, s in sorted(scores.items()):
    t = sum(s.values())
    cond = name.split("_")[0]
    totals[cond].append(t)
    print(f"{name:<12}{s['H1']:>3}{s['H2']:>3}{s['H3']:>3}{s['H4']:>3}{s['H5']:>3}{s['H6']:>3}{t:>4}")
print()
for cond in ["EN", "ZH"]:
    v = totals[cond]
    print(f"{cond}: n={len(v)}  均值={sum(v)/len(v):.3f}  sd={ (sum((x-sum(v)/len(v))**2 for x in v)/(len(v)-1))**0.5:.3f}  min={min(v)} max={max(v)}")

print("\n需人工复核的标记：")
for name, msgs in sorted(h_flags.items()):
    print(f"  {name}: {'; '.join(msgs)}")

# H5 立场分布
dist = collections.Counter((n.split('_')[0], v['stance']) for n, v in h5.items())
print("\nH5 立场分布:", dict(dist))
