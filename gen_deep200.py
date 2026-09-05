import os as _os
BASE = _os.path.dirname(_os.path.abspath(__file__))
"""200 步终极压力测试：同 50 步设计，步数 x4"""
import json
import random

random.seed(20260906)
DIGITS_CN = "零一二三四五六七八九"
ONES_EN = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
           "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
           "seventeen", "eighteen", "nineteen"]
TENS_EN = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
BASE = BASE
N = 200


def cn_num(n):
    h, t, o = n // 100, (n % 100) // 10, n % 10
    s = ""
    if h:
        s += DIGITS_CN[h] + "百"
    if t:
        s += DIGITS_CN[t] + "十"
    elif h and o:
        s += "零"
    if o:
        s += DIGITS_CN[o]
    return s or "零"


def en_num(n):
    h, rem = n // 100, n % 100
    parts = []
    if h:
        parts.append(ONES_EN[h] + " hundred")
    if rem:
        if h:
            parts.append("and")
        if rem < 20:
            parts.append(ONES_EN[rem])
        else:
            t, o = rem // 10, rem % 10
            parts.append(TENS_EN[t] + ("-" + ONES_EN[o] if o else ""))
    return " ".join(parts)


ops = [(random.choice([1, -1]), random.randint(1, 999)) for _ in range(N)]
x, steps = 0, []
for sign, v in ops:
    x += sign * v
    steps.append(x)

# 中文版
lines = ["# 长链计算（200 步 · 中文表述）", "",
         "请从 0 开始，严格按照下面的顺序依次执行全部操作，求出最终的结果数值。", "",
         "**要求**：必须逐步计算，每一步都写出累积值。不要跳步，不要合并步骤，不要使用任何工具。",
         "", "操作序列："]
for i, (sign, v) in enumerate(ops, 1):
    lines.append(f"{i}. {'加' if sign > 0 else '减'}{cn_num(v)}")
lines += ["", "请给出每一步后的累积值，以及最终结果。"]
open(f"{BASE}/deep_cn_200.md", "w", encoding="utf-8").write("\n".join(lines))

# 英文版
lines = ["# Long-chain computation (200 steps · English wording)", "",
         "Starting from 0, perform all operations strictly in order and give the final result.", "",
         "**Requirement**: compute step by step, writing the running total after every step. "
         "Do not skip or merge steps, do not use any tools.", "", "Operations:"]
for i, (sign, v) in enumerate(ops, 1):
    lines.append(f"{i}. {'add' if sign > 0 else 'subtract'} {en_num(v)}")
lines += ["", "Give the running total after each step, and the final result."]
open(f"{BASE}/deep_en_200.md", "w", encoding="utf-8").write("\n".join(lines))

json.dump({"steps": steps, "final": x, "ops": ops},
          open(f"{BASE}/deep_gold_200.json", "w"), ensure_ascii=False, indent=1)
print(f"[200 步] 金标准最终值 = {x}")
print(f"  中间值范围: {min(steps)} ~ {max(steps)}")
print(f"  前 3 步: {steps[:3]}")
