import matplotlib.pyplot as plt
import numpy as np

area = np.array([30, 35, 42, 45, 50, 55, 60,
                 65, 70, 75, 80, 90, 100, 110])

price = np.array([6.2, 7.0, 8.1, 8.5, 9.3, 10.5, 11.2,
                  12.1, 13.0, 14.5, 15.0, 17.2, 19.1, 21.0])

rooms = np.array([1, 1, 1, 2, 2, 2, 2,
                  2, 3, 3, 3, 3, 4, 4])


# 1. Зависимость стоимости от площади
fig, ax = plt.subplots()

ax.scatter(area, price, color="blue", s=70, alpha=0.7)
ax.set_title("Зависимость стоимости квартиры от площади")
ax.set_xlabel("Площадь квартиры, м²")
ax.set_ylabel("Стоимость, млн руб.")
ax.grid(True)

plt.show()


# 2. Цвет и размер точек по количеству комнат
fig, ax = plt.subplots()

our_color = ax.scatter(
    area,
    price,
    c=rooms,
    cmap="viridis",
    s=[r ** 2 * 60 for r in rooms]
)

fig.colorbar(our_color, label="Количество комнат")

ax.set_title("Стоимость квартир по площади и числу комнат")
ax.set_xlabel("Площадь квартиры, м²")
ax.set_ylabel("Стоимость, млн руб.")

plt.show()
