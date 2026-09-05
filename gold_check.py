import itertools

# Q1: a1=2, a2=5, a(n) = (a(n-1)+a(n-2)) % 10
a = [0, 2, 5]
for n in range(3, 2100):
    a.append((a[n - 1] + a[n - 2]) % 10)
print("Q1 a46 =", a[46], " a2026 =", a[2026], " a(2026 mod 60) idx:", 2026 % 60)
# find period
for p in range(1, 300):
    if all(a[i] == a[i + p] for i in range(1, 200)):
        print("Q1 period =", p)
        break

# Q2: ranking puzzle
people = ["甲", "乙", "丙", "丁", "戊"]
idx = {p: i for i, p in enumerate(people)}


def stmt(rank_of, speaker):
    # rank_of[p] = 1..5
    if speaker == "甲":
        return rank_of["甲"] != 5
    if speaker == "乙":
        return rank_of["丙"] == 1
    if speaker == "丙":
        return rank_of["丁"] != 2
    if speaker == "丁":
        return rank_of["戊"] == 3
    if speaker == "戊":
        return rank_of["乙"] == 5


sols = []
for perm in itertools.permutations(people):
    rank_of = {p: perm.index(p) + 1 for p in people}
    if all(stmt(rank_of, sp) == (rank_of[sp] <= 2) for sp in people):
        sols.append(rank_of)
print("Q2 solutions:", len(sols))
for s in sols:
    print("  ", sorted(s.items(), key=lambda x: x[1]))

# Q10: recipe
total = 0.75 * 2.5
print("Q10 total cups =", total)
q = int(total // 0.25)
rem = total - q * 0.25
tbsp = rem * 16
print(f"Q10 = {q} quarter-cups + {tbsp} tablespoons")
