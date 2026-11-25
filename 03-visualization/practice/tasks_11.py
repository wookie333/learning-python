import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("tips")

# EDA

print(df.shape)
df.info()

print(df.isna().sum())
print(df.describe())

mean_tip = df.groupby("day", observed=True)["tip"].mean()
print(mean_tip)

df["tip_percent"] = df["tip"] / df["total_bill"] * 100

print(df.head())
print(df.groupby("day", observed=True)["tip_percent"].mean())

# Visualization

fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 10))

sns.histplot(
    data=df, x="total_bill",
    ax=axes[0, 0], kde=True
)
axes[0, 0].set_title("Total bill distribution")

sns.boxplot(
    data=df, x="day", y="tip",
    ax=axes[0, 1]
)
axes[0, 1].set_title("Tips by day")

sns.scatterplot(
    data=df, x="total_bill", y="tip",
    ax=axes[0, 2], hue="time", s=20, alpha=0.7
)
axes[0, 2].set_title("Total bill vs Tips")

sns.barplot(
    data=df, x="day", y="tip_percent",
    ax=axes[1, 0]
)
axes[1, 0].set_title("Average tip percentage by day")

sns.regplot(
    data=df, x="total_bill", y="tip",
    ax=axes[1, 1], ci=None,
    scatter_kws={"alpha": 0.7}
)
axes[1, 1].set_title("Linear regression")

corr = df.select_dtypes(include="number").corr()

sns.heatmap(
    data=corr, annot=True,
    vmin=-1, vmax=1, cmap="coolwarm",
    fmt=".2f", ax=axes[1, 2]
)
axes[1, 2].set_title("Correlation matrix")

print(corr)

fig.suptitle("Restaurant Tips — Exploratory Data Analysis")
fig.tight_layout()
plt.show()

# Conclusions:
# 1. Total bill has a right-skewed distribution.
# 2. Friday has the highest average tip percentage.
# 3. Total bill and tip have a positive correlation (~0.68).
# 4. A larger bill does not guarantee a higher tip percentage.
# 5. Correlation does not imply causation.
#
# ML note:
# If predicting tip, tip_percent must not be used as a feature,
# because it is calculated from the target variable.
# This would cause target leakage.
