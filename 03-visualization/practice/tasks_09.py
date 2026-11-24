import numpy as np
import matplotlib.pyplot as plt

area = [30, 45, 55, 70, 90, 110]
rooms = [1, 2, 2, 3, 4, 5]
price = [6, 9, 11, 15, 18, 22]
metro = [25, 20, 22, 12, 8, 5]

labels = ["area", "rooms", "price", "metro"]

together = np.column_stack((area, rooms, price, metro)).T
corr = np.corrcoef(together)

fig, ax = plt.subplots()

im = ax.imshow(
    corr,
    cmap="coolwarm",
    vmin=-1,
    vmax=1
)

for i in range(corr.shape[0]):
    for j in range(corr.shape[1]):
        value = corr[i, j]

        ax.text(
            j, i, f"{value:.2f}",
            ha="center",
            va="center",
            color="white" if abs(value) > 0.7 else "black"
        )

ax.set_xticks(range(len(labels)), labels)
ax.set_yticks(range(len(labels)), labels)
ax.set_title("Correlation matrix")

fig.colorbar(
    im,
    ax=ax,
    ticks=[-1, -0.5, 0, 0.5, 1],
    label="Correlation Coefficient"
)

print(np.round(corr, 2))

fig.tight_layout()
plt.show()
