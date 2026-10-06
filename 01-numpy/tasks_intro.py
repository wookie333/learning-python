import numpy as np

# Задача 1: Индексация
a = np.array([10, 20, 30, 40, 50])
print(a[0])
print(a[-1])
print(a[::2], '\n')

# Задача 2: Boolean indexing (2 способа)
our_massiv = np.array([1, -2, 3, -4, 5])

# Способ 1: цикл
for x in our_massiv:
    if x > 0:
        print(x)

# Способ 2: Boolean indexing
print(our_massiv[our_massiv > 0], '\n')

# Задача 3: Reshape
new_massiv = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(new_massiv.reshape(3, 4))
