import matplotlib.pyplot as plt


# Задача 1. Продажи двух магазинов
#
# Условие:
# Построить два графика рядом:
# 1. Линейный график продаж магазина A с маркерами.
# 2. Столбчатый график продаж магазина B.
# Использовать figsize=(12, 5), sharey=True,
# отдельные заголовки и общий заголовок.


days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]

shop_a = [120, 135, 110, 160, 175, 190, 200]
shop_b = [90, 100, 115, 130, 125, 150, 170]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), sharey=True)

ax1.plot(days, shop_a, marker="o")
ax1.set_title("Shop A")

ax2.bar(days, shop_b)
ax2.set_title("Shop B")

fig.suptitle("Продажи магазинов за неделю")
fig.tight_layout()
plt.show()


# Задача 2. Аналитика кофейни
#
# Условие:
# Построить дашборд 2x2 размером (12, 8):
# 1. Линейный график посещаемости с маркерами.
# 2. Столбчатый график выручки.
# 3. Pie с продажами напитков и процентами.
# 4. Scatter зависимости выручки от посетителей.
# Добавить заголовки, подписи осей и tight_layout().


days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
visitors = [85, 92, 110, 105, 135, 170, 155]
revenue = [12500, 13800, 16500, 15700, 20500, 26000, 23500]

drinks = ["Кофе", "Чай", "Лимонад", "Сок"]
sales = [55, 20, 15, 10]

fig, ax = plt.subplots(2, 2, figsize=(12, 8))

ax[0, 0].plot(days, visitors, marker="o")
ax[0, 0].set_title("Visitors")

ax[0, 1].bar(days, revenue)
ax[0, 1].set_title("Revenue")

ax[1, 0].pie(sales, autopct="%1.0f%%", labels=drinks, startangle=90)
ax[1, 0].set_title("Drinks")

ax[1, 1].scatter(visitors, revenue)
ax[1, 1].set_xlabel("Visitors")
ax[1, 1].set_ylabel("Revenue, rub.")
ax[1, 1].set_title("Зависимость выручки от количества посетителей")

fig.suptitle("Аналитика кофейни")
fig.tight_layout()
plt.show()


# Задача 3. Визуализация ML-предсказаний
#
# Условие:
# Построить два графика рядом, figsize=(12, 5).
# Слева — scatter реальных и предсказанных цен
# с линией идеальных предсказаний y = x.
# Справа — график изменения loss по эпохам.
# Добавить легенду, подписи осей и заголовки.


actual = [3.2, 4.5, 5.1, 6.0, 7.3, 8.1, 9.5]
predicted = [3.4, 4.2, 5.3, 5.8, 7.0, 8.5, 9.1]

epochs = [1, 2, 3, 4, 5, 6, 7]
loss = [4.8, 3.2, 2.1, 1.4, 0.9, 0.6, 0.4]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.scatter(actual, predicted, label="Predicted")
ax1.plot(actual, actual, label="Ideal predictions")
ax1.set_xlabel("Actual")
ax1.set_ylabel("Predicted")
ax1.set_title("Actual vs Predicted")
ax1.legend()

ax2.plot(epochs, loss, marker="o")
ax2.set_xlabel("Epochs")
ax2.set_ylabel("Loss")
ax2.set_title("Training Loss")

fig.suptitle("Предсказание стоимости квартир")
fig.tight_layout()
plt.show()
