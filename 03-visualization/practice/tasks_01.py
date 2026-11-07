import matplotlib.pyplot as plt


# Задача 1. Количество заказов за неделю
# Построить один линейный график через объектный стиль Matplotlib.

days = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
orders = [25, 32, 28, 45, 51, 68, 59]

fig, ax = plt.subplots(figsize=(9, 4))

ax.plot(days, orders)
ax.set_title("Количество заказов за неделю")
ax.set_xlabel("День недели")
ax.set_ylabel("Заказы")

plt.show()


# Задача 2. Выручка и расходы
# Построить два графика рядом в одной Figure.

quarters = [1, 2, 3, 4]
revenue = [120, 150, 140, 190]
expenses = [80, 95, 110, 125]

fig, axes = plt.subplots(1, 2, figsize=(10, 4))

axes[0].plot(quarters, revenue)
axes[0].set_title("Выручка")

axes[1].plot(quarters, expenses)
axes[1].set_title("Расходы")

plt.show()


# Задача 3. Сетка графиков 2x3
# Способ 1. Ручное обращение к каждому объекту Axes.

x = [1, 2, 3]
y = [3, 7, 5]

fig, axes = plt.subplots(2, 3, figsize=(12, 6))

axes[0, 0].plot(x, y)
axes[0, 0].set_title("График 1")

axes[0, 1].plot(x, y)
axes[0, 1].set_title("График 2")

axes[0, 2].plot(x, y)
axes[0, 2].set_title("График 3")

axes[1, 0].plot(x, y)
axes[1, 0].set_title("График 4")

axes[1, 1].plot(x, y)
axes[1, 1].set_title("График 5")

axes[1, 2].plot(x, y)
axes[1, 2].set_title("График 6")

fig.tight_layout()
plt.show()


# Задача 3. Способ 2
# Построение тех же шести графиков через enumerate().

fig, axes = plt.subplots(2, 3, figsize=(12, 6))

# axes.flat перебирает все Axes слева направо, сверху вниз.
# enumerate() добавляет номер каждому графику, начиная с 1.

for i, ax in enumerate(axes.flat, start=1):
    ax.plot(x, y)
    ax.set_title(f"График {i}")

fig.tight_layout()
plt.show()
