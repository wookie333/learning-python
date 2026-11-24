import numpy as np
import matplotlib.pyplot as plt

district_a = np.array([
    8, 9, 10, 10, 11, 12, 12, 13, 14, 45
])

district_b = np.array([
    12, 13, 14, 15, 15, 16, 17, 18, 19, 20
])

prices = np.concatenate((district_a, district_b))

fig, ax = plt.subplots()

ax.hist(
    prices,
    bins=10,
    density=True,
    edgecolor="black"
)

ax.set_title("Распределение цен")
ax.set_xlabel("Стоимость, млн рублей")
ax.set_ylabel("Плотность")
ax.grid(True)

fig, ax = plt.subplots()

ax.boxplot(
    [district_a, district_b],
    tick_labels=["Район А", "Район Б"],
    showmeans=True,
    orientation="horizontal"
)

ax.set_title("Сравнение районов")
ax.set_xlabel("Стоимость, млн рублей")
ax.grid(True)

Q1 = np.percentile(district_a, 25)
Q3 = np.percentile(district_a, 75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = district_a[
    (district_a < lower_bound) |
    (district_a > upper_bound)
]

print(f"Q1: {Q1}")
print(f"Q3: {Q3}")
print(f"IQR: {IQR}")

print(f"Lower bound: {lower_bound}")
print(f"Upper bound: {upper_bound}")
print(f"Outliers: {outliers}")

print(f"District A mean: {np.mean(district_a)}")
print(f"District A median: {np.median(district_a)}")

print(f"District B mean: {np.mean(district_b)}")
print(f"District B median: {np.median(district_b)}")

plt.show()
