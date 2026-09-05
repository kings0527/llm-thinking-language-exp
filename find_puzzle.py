import itertools

people = ["甲", "乙", "丙", "丁", "戊"]
perms = list(itertools.permutations([1, 2, 3, 4, 5]))  # perm[i] = rank of people[i]

# candidate statements: (label, text, function(rank_of)->bool)
cands = [
    ("甲不是最后一名", lambda r: r["甲"] != 5),
    ("丙是第一名", lambda r: r["丙"] == 1),
    ("丁不是第二名", lambda r: r["丁"] != 2),
    ("戊是第三名", lambda r: r["戊"] == 3),
    ("乙是第五名", lambda r: r["乙"] == 5),
    ("甲是第二名", lambda r: r["甲"] == 2),
    ("乙不是第一名", lambda r: r["乙"] != 1),
    ("丙的名次比丁差", lambda r: r["丙"] > r["丁"]),
    ("戊不是最后一名", lambda r: r["戊"] != 5),
    ("甲的名次比乙靠前", lambda r: r["甲"] < r["乙"]),
    ("丁是第四名", lambda r: r["丁"] == 4),
    ("丙不是最后一名", lambda r: r["丙"] != 5),
    ("乙的名次比戊靠前", lambda r: r["乙"] < r["戊"]),
    ("丁的名次比甲靠前", lambda r: r["丁"] < r["甲"]),
    ("丙是第二名", lambda r: r["丙"] == 2),
    ("戊是第二名", lambda r: r["戊"] == 2),
]
who = ["甲", "乙", "丙", "丁", "戊"]

# precompute: for candidate c assigned to speaker i -> 120-bit mask of perms where t(c,q)==req(q,i)
masks = {}
for ci, (label, fn) in enumerate(cands):
    for i, sp in enumerate(who):
        m = 0
        for qi, perm in enumerate(perms):
            r = {who[j]: perm[j] for j in range(5)}
            req = r[sp] <= 2
            if fn(r) == req:
                m |= 1 << qi
        masks[(ci, i)] = m

best = []
n = len(cands)
for combo in itertools.permutations(range(n), 5):
    m = masks[(combo[0], 0)]
    for i in range(1, 5):
        m &= masks[(combo[i], i)]
        if m == 0:
            break
    if m and m.bit_count() == 1:
        qi = (m & -m).bit_length() - 1
        best.append((combo, perms[qi]))

print("unique-solution combos found:", len(best))
for combo, sol in best[:12]:
    txt = " ; ".join(f"{who[i]}说‘{cands[combo[i]][0]}’" for i in range(5))
    print(f"\n{txt}\n   -> 唯一解: " + ", ".join(f"{who[i]}第{sol[i]}名" for i in range(5)))
