import itertools

# H2: 7-digit numbers from digits 1-7 each once, divisible by 11
cnt = 0
for p in itertools.permutations(range(1, 8)):
    n = int("".join(map(str, p)))
    if n % 11 == 0:
        cnt += 1
print("H2 答案（能被11整除的七位数个数）=", cnt)
# analytic check
from itertools import combinations
groups = [c for c in combinations(range(1, 8), 3) if sum(c) == 14]
print("  偶数位(3位)和为14的三元组:", groups, "组数:", len(groups))
print("  解析解:", len(groups) * 6 * 24)

# H4: knights and knaves
# A: "B is a knave" ; B: "A and C are the same type" ; C: "A is a knight"
sols = []
for a, b, c in itertools.product([True, False], repeat=3):  # True = knight
    sA = (b == False)
    sB = (a == c)
    sC = (a == True)
    if (sA == a) and (sB == b) and (sC == c):
        sols.append((a, b, c))
print("\nH4 解 (A,B,C; True=骑士):", sols)
