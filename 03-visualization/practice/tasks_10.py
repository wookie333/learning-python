import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
n = 200

df = pd.DataFrame({
    "genre": rng.choice(
        ["Action", "Comedy", "Drama", "Horror", "Fantasy"],
        size=n
    ),
    "year": rng.integers(2000, 2025, size=n),
    "rating": np.round(
        rng.normal(6.5, 1.2, size=n).clip(1, 10), 1
    ),
    "budget": np.round(
        rng.uniform(5, 150, size=n), 1
    )
})

df["revenue"] = np.round(
    df["budget"] * rng.uniform(0.3, 3, size=n), 1
)

print(df.shape)
df.info()
print(df.isna().sum())
print(df.describe())

rating_by_genre = df.groupby("genre")["rating"].mean()
movies_per_year = df["year"].value_counts().sort_index()

print(rating_by_genre)
print(movies_per_year)

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0, 0].plot(
    movies_per_year.index,
    movies_per_year.values,
    marker="o"
)
axes[0, 0].set_title("Movies per year")
axes[0, 0].set_xlabel("Year")
axes[0, 0].set_ylabel("Number of movies")

axes[0, 1].bar(
    rating_by_genre.index,
    rating_by_genre.values
)
axes[0, 1].set_title("Average rating by genre")
axes[0, 1].set_xlabel("Genre")
axes[0, 1].set_ylabel("Rating")

axes[1, 0].hist(
    df["rating"],
    bins=15,
    edgecolor="black"
)
axes[1, 0].set_title("Rating distribution")
axes[1, 0].set_xlabel("Rating")
axes[1, 0].set_ylabel("Frequency")

axes[1, 1].scatter(
    df["budget"],
    df["revenue"],
    alpha=0.7
)
axes[1, 1].set_title("Budget vs Revenue")
axes[1, 1].set_xlabel("Budget, million USD")
axes[1, 1].set_ylabel("Revenue, million USD")

for ax in axes.flat:
    ax.grid(True, alpha=0.3)

corr = df["revenue"].corr(df["budget"])
print(f"Correlation: {corr:.4f}")

print("Movie with maximum revenue:")
print(df.loc[df["revenue"].idxmax()])

percent = (df["revenue"] > df["budget"]).mean() * 100
print(f"Revenue above budget: {percent:.2f}%")

fig.suptitle("Movie Data Analysis")
fig.tight_layout()
plt.show()
