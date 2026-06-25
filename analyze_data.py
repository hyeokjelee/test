import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

plt.rcParams["font.family"] = fm.FontManager().ttflist[0].name
plt.rcParams["axes.unicode_minus"] = False

# ── 데이터 로드 ──────────────────────────────────────────────
df = pd.read_csv("sample_data.csv")
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M")

# ── 1. 기본 통계 ─────────────────────────────────────────────
print("=== 기본 통계 ===")
print(df[["amount", "score"]].describe())
print()

# ── 2. 카테고리 분석 ─────────────────────────────────────────
print("=== 카테고리별 분석 ===")
cat_stats = df.groupby("category").agg(
    total_amount=("amount", "sum"),
    avg_amount=("amount", "mean"),
    avg_score=("score", "mean"),
    count=("id", "count"),
).round(2)
print(cat_stats)
print()

# ── 3. 점수 분포 ─────────────────────────────────────────────
print("=== 점수 분포 ===")
score_bins = [0, 60, 70, 80, 90, 100]
score_labels = ["0-60", "61-70", "71-80", "81-90", "91-100"]
df["score_group"] = pd.cut(df["score"], bins=score_bins, labels=score_labels, right=False)
print(df["score_group"].value_counts().sort_index())
print()

# ── 4. 월별 추이 ─────────────────────────────────────────────
print("=== 월별 추이 ===")
monthly = df.groupby("month").agg(
    total_amount=("amount", "sum"),
    avg_score=("score", "mean"),
    count=("id", "count"),
).round(2)
print(monthly)

# ── 시각화 ───────────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 카테고리별 총 지출
ax1 = axes[0, 0]
cat_stats.sort_values("total_amount", ascending=True).plot.barh(
    y="total_amount", ax=ax1, color="#4C72B0"
)
ax1.set_title("카테고리별 총 지출")
ax1.set_xlabel("총 지출 (원)")

# 점수 분포 히스토그램
ax2 = axes[0, 1]
df["score"].hist(bins=10, ax=ax2, color="#55A868", edgecolor="white")
ax2.set_title("점수 분포")
ax2.set_xlabel("점수")
ax2.set_ylabel("빈도")

# 월별 지출 추이
ax3 = axes[1, 0]
monthly["total_amount"].plot(ax=ax3, marker="o", color="#C44E52")
ax3.set_title("월별 지출 추이")
ax3.set_xlabel("월")
ax3.set_ylabel("총 지출 (원)")

# 카테고리별 평균 점수
ax4 = axes[1, 1]
cat_stats.sort_values("avg_score", ascending=True).plot.barh(
    y="avg_score", ax=ax4, color="#8172B3"
)
ax4.set_title("카테고리별 평균 점수")
ax4.set_xlabel("평균 점수")

plt.tight_layout()
plt.savefig("analysis_results.png", dpi=150)
print("\n분석 결과 시각화: analysis_results.png")
