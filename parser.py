import os as _os
BASE = _os.path.dirname(_os.path.abspath(__file__))
import os
import re

RUNS = BASE + "/runs"
HDR = re.compile(r"^#{1,4}\s*\*{0,2}Q(\d+)", re.M)


def parse_blocks(text):
    """Split a run file into {qnum: block_text} using real markdown headers only."""
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


def load_all():
    data = {}
    for fn in sorted(f for f in os.listdir(RUNS) if f.endswith(".md")):
        raw = open(os.path.join(RUNS, fn), encoding="utf-8").read()
        data[fn[:-3]] = parse_blocks(raw)
    return data
