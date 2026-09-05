import os as _os
BASE = _os.path.dirname(_os.path.abspath(__file__))
"""把实验脚本中硬编码的绝对路径替换为基于脚本位置的 BASE，使仓库可移植。"""
import os
import re

D = BASE
ABS = BASE
HEADER = "import os as _os\nBASE = _os.path.dirname(_os.path.abspath(__file__))\n"

patched = []
for fn in sorted(os.listdir(D)):
    if not fn.endswith(".py"):
        continue
    p = os.path.join(D, fn)
    src = open(p, encoding="utf-8").read()
    if ABS not in src:
        continue
    # 规则 a：BASE 定义行  X = "<abs>"  ->  X = BASE
    src2 = re.sub(r'(\w+)\s*=\s*"' + re.escape(ABS) + '"', r"\1 = BASE", src)
    # 规则 b：其余出现  "<abs>...  ->  BASE + "...
    src2 = src2.replace('"' + ABS, 'BASE + "')
    if src2 != src:
        if not src2.startswith(HEADER.strip()):
            src2 = HEADER + src2
        open(p, "w", encoding="utf-8").write(src2)
        patched.append(fn)

print("已修补:", patched)
# 验证：不再有绝对路径
left = []
for fn in patched:
    if ABS in open(os.path.join(D, fn), encoding="utf-8").read():
        left.append(fn)
print("残留绝对路径:", left or "无")
