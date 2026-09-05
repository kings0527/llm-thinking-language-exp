import os as _os
BASE = _os.path.dirname(_os.path.abspath(__file__))
"""生成深度长链推理题：同一组数字序列的三种语言表述（中文/英文/阿拉伯）
用途：分离"任务表述语言"与"思考语言"的效应。50 步长链可定位首次出错步数。"""
import random
import json

random.seed(20260905)

DIGITS_CN = "零一二三四五六七八九"
ONES_EN = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
           "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
           "seventeen", "eighteen", "nineteen"]
TENS_EN = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


def cn_num(n):
    assert 0 <= n <= 999
    if n == 0:
        return "零"
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
    return s


def en_num(n):
    assert 0 <= n <= 999
    if n == 0:
        return "zero"
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


def gen(n_steps=50, maxv=999):
    ops = []
    for _ in range(n_steps):
        ops.append((random.choice([1, -1]), random.randint(1, maxv)))
    return ops


def accumulate(ops):
    x, steps = 0, []
    for sign, v in ops:
        x += sign * v
        steps.append(x)
    return x, steps


# ---------- 生成三组题（同一序列的三种表述）----------
N_STEPS_LIST = [20, 50]
BASE = BASE
GOLD = {}

for n_steps in N_STEPS_LIST:
    ops = gen(n_steps)
    final, steps = accumulate(ops)
    GOLD[str(n_steps)] = {"ops": ops, "steps": steps, "final": final}

    # 中文表述
    lines = [f"# 长链计算（{n_steps} 步 · 中文表述）", "",
             "请从 0 开始，严格按照下面的顺序依次执行全部操作，求出最终的结果数值。",
             "", "**要求**：必须逐步计算，每一步都写出“第 k 步后 = X”这样的累积值，最后单独给出最终答案。",
             "不要跳步，不要合并步骤，不要使用任何工具。", "", "操作序列："]
    for i, (sign, v) in enumerate(ops, 1):
        lines.append(f"{i}. {'加' if sign > 0 else '减'}{cn_num(v)}")
    lines += ["", "请给出每一步后的累积值，以及最终结果。"]
    open(f"{BASE}/deep_cn_{n_steps}.md", "w", encoding="utf-8").write("\n".join(lines))

    # 英文表述（相同数字）
    lines = [f"# Long-chain computation ({n_steps} steps · English wording)", "",
             "Starting from 0, perform all of the following operations strictly in the given order, and give the final result.",
             "", "**Requirement**: compute step by step. For every step write the running total in the form "
                 "\"After step k = X\". Finally state the final answer on its own line.",
             "Do not skip steps, do not merge steps, do not use any tools.", "", "Operations:"]
    for i, (sign, v) in enumerate(ops, 1):
        lines.append(f"{i}. {'add' if sign > 0 else 'subtract'} {en_num(v)}")
    lines += ["", "Give the running total after each step, and the final result."]
    open(f"{BASE}/deep_en_{n_steps}.md", "w", encoding="utf-8").write("\n".join(lines))

    # 阿拉伯数字表述（语言中性基线，相同数字）
    lines = [f"# 长链计算（{n_steps} 步 · 数字表述）", "",
             "请从 0 开始，严格按照下面的顺序依次执行全部操作，求出最终的结果数值。",
             "", "**要求**：必须逐步计算，每一步都写出“第 k 步后 = X”这样的累积值，最后单独给出最终答案。",
             "不要跳步，不要合并步骤，不要使用任何工具。", "", "操作序列："]
    for i, (sign, v) in enumerate(ops, 1):
        lines.append(f"{i}. {'+' if sign > 0 else '-'}{v}")
    lines += ["", "请给出每一步后的累积值，以及最终结果。"]
    open(f"{BASE}/deep_num_{n_steps}.md", "w", encoding="utf-8").write("\n".join(lines))

    print(f"[{n_steps} 步] 最终金标准 = {final}")
    print(f"  前 5 步累积: {steps[:5]}")
    print(f"  中间值范围: {min(steps)} ~ {max(steps)}")

json.dump(GOLD, open(f"{BASE}/deep_gold.json", "w"), ensure_ascii=False, indent=1)
print("\n金标准已保存 deep_gold.json")
