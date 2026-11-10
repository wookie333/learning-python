import matplotlib.pyplot as plt

# Продажи магазина: факт и план
days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]

fact = [120, 135, 128, 155, 170, 210, 190]
plan = [130, 130, 140, 150, 160, 180, 200]

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(days, fact, color="g", marker="o",
        linewidth=2.5, label="Факт")

ax.plot(days, plan, color="r", marker="s",
        linewidth=1.5, linestyle="--",
        alpha=0.5, label="План")

ax.set_title("Фактические продажи превысили план в 4 из 7 дней")
ax.set_xlabel("День недели")
ax.set_ylabel("Выручка, тыс. руб.")

ax.set_ylim(0, 250)
ax.tick_params(axis="x", labelrotation=30)
ax.grid(True, axis="y", linestyle="--", alpha=0.3)
ax.legend()

plt.show()
