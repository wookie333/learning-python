import numpy as np
import matplotlib.pyplot as plt

epochs = np.arange(1, 9)

train_loss = np.array([
    0.92, 0.74, 0.61, 0.50,
    0.43, 0.37, 0.33, 0.29
])

val_loss = np.array([
    0.98, 0.79, 0.66, 0.57,
    0.51, 0.49, 0.53, 0.60
])


# Task 1: Training and validation loss

fig, ax = plt.subplots(figsize=(8, 4))

ax.plot(epochs, train_loss, label="Train Loss", color="blue", marker="o")
ax.plot(epochs, val_loss, label="Validation Loss", color="red", marker="o")

ax.set_xlabel("Epochs")
ax.set_ylabel("Loss")
ax.set_title("Model Training Loss")

ax.grid(True, axis="y", alpha=0.2)
ax.legend()

fig.savefig("training_loss.png", dpi=200, bbox_inches="tight")
plt.show()


# Task 2: Best epoch and loss gap

fig, ax = plt.subplots(figsize=(8, 4))

best = np.argmin(val_loss)

ax.plot(epochs, train_loss, label="Train Loss", color="blue", marker="o")
ax.plot(epochs, val_loss, label="Validation Loss", color="red", marker="o")

ax.annotate(
    "Best loss",
    xy=(epochs[best], val_loss[best]),
    xytext=(epochs[best] - 2, val_loss[best] + 0.2),
    arrowprops=dict(arrowstyle="->", color="black")
)

ax.axvline(epochs[best], color="red", linestyle="--", alpha=0.5)

ax.fill_between(
    epochs,
    train_loss,
    val_loss,
    color="blue",
    alpha=0.2
)

ax.set_xlabel("Epochs")
ax.set_ylabel("Loss")
ax.set_title("Best Validation Epoch")

ax.grid(True, axis="y", alpha=0.2)
ax.legend()

fig.savefig("best_epoch.png", dpi=200, bbox_inches="tight")
plt.show()
