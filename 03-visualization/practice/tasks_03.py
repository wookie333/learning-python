import matplotlib.pyplot as plt
import numpy as np

categories = ["Телефоны", "Ноутбуки", "Наушники", "Планшеты"]
sales = [320, 180, 450, 210]

checks = np.array([
    120, 200, 240, 300, 320, 360, 400,
    450, 510, 550, 620, 700, 850, 900
])

# 1. Продажи по категориям
fig, ax = plt.subplots(figsize=(8, 4))

bars = ax.bar(categories, sales, color="green", edgecolor="black")

ax.set_title("Продажи по категориям")
ax.set_ylabel("Количество продаж, шт.")
ax.bar_label(bars, fmt="%d")
ax.set_ylim(0, 500)

plt.tight_layout()
plt.show()


# 2. Распределение чеков
fig, ax = plt.subplots(figsize=(8, 4))

counts, edges, patches = ax.hist(
    checks,
    bins=[0, 200, 400, 600, 800, 1000],
    color="blue",
    edgecolor="black"
)

ax.set_title("Распределение чеков покупателей")
ax.set_xlabel("Сумма чека, руб.")
ax.set_ylabel("Количество покупок")

ax.axvline(
    checks.mean(),
    color="red",
    linestyle="--",
    linewidth=2,
    label=f"Средний чек: {checks.mean():.0f} руб."
)

ax.legend()

print("Counts:", counts)
print("Edges:", edges)
print("Всего чеков:", int(counts.sum()))

plt.tight_layout()
plt.show()
