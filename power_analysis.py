import math

# 功效分析：基于第二轮实测方差，估算检测不同效应量所需的重复轮数
# 第二轮分数（满分 12）：EN 11,11,12 / ZH 12,11,12 / NAT 11,12,12 / ADAPT 11,11,12
groups = {
    "EN": [11, 11, 12], "ZH": [12, 11, 12],
    "NAT": [11, 12, 12], "ADAPT": [11, 11, 12],
}
MAXS = 12.0

ss, df = 0.0, 0
for g, v in groups.items():
    m = sum(v) / len(v)
    ss += sum((x - m) ** 2 for x in v)
    df += len(v) - 1
var = ss / df
sd = math.sqrt(var)
print(f"合并组内方差 = {var:.4f}  标准差 = {sd:.4f}  (满分 {MAXS:.0f}，变异系数 {sd/MAXS*100:.1f}%)")

Z_A, Z_B = 1.959964, 0.8416212  # alpha=.05 双侧, power=80%

print("\n【需要多少轮？】两独立样本 t 检验，alpha=.05、功效 80%")
print(f"{'欲检测的准确率差异':<22}{'绝对分差(12分制)':>18}{'每组所需轮数':>14}")
for pct in [0.15, 0.10, 0.08, 0.05, 0.04, 0.03, 0.02, 0.01, 0.011]:
    delta = MAXS * pct
    n = 2 * (Z_A + Z_B) ** 2 * var / delta ** 2
    print(f"{pct*100:>18.1f}%{delta:>18.2f}{math.ceil(n):>14d}")

print("\n【当前观测到的差异意味着什么】")
obs = 0.34 / 32  # 两轮合计 32 分制下观测到的极差
print(f"  实测四条件极差 = 0.34 / 32 = {obs*100:.2f}%")
n_need = 2 * (Z_A + Z_B) ** 2 * var / (MAXS * obs) ** 2
def mde(n):
    """给定每组轮数 n，返回可检测的最小差异（占满分的百分比）"""
    return math.sqrt(2 * (Z_A + Z_B) ** 2 * var / n) / MAXS * 100


print(f"  要让这个差异达到统计显著，每组需要约 {math.ceil(n_need)} 轮")
print("\n【反过来：给定轮数，能检测多大的差异？】")
for n in [3, 6, 10, 20, 30, 50, 100, 322]:
    print(f"  每组 {n:>3d} 轮 → 可检测 ≥ {mde(n):>5.2f}% 的准确率差异")

print("\n【另一种情况：题目变难会怎样】")
print("  若题目难度上升使标准差翻倍（模型开始出现真实失误），方差 x4：")
for pct in [0.10, 0.05, 0.03]:
    delta = MAXS * pct
    n = 2 * (Z_A + Z_B) ** 2 * (var * 4) / delta ** 2
    print(f"    检测 {pct*100:>4.0f}% 差异 → 每组 {math.ceil(n):>4d} 轮")
