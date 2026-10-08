import numpy as np

# Задача 1: Типы данных
# Создай массив [1, 2, 3, 4] с типами int8, int16, float32.
# Выведи dtype каждого.

mass1 = np.array([1, 2, 3, 4], dtype='int8')
mass2 = np.array([1, 2, 3, 4], dtype='int16')
mass3 = np.array([1, 2, 3, 4], dtype='float32')
print(mass1.dtype, mass2.dtype, mass3.dtype)


# Задача 2: Переполнение int8
# Создай массив [100, 200, 300] с dtype='int8'.
# Что произойдет? Почему?

'''our_massiv = np.array([100, 200, 300], dtype='int8')
print(our_massiv)'''
'''Произойдет переполнение => сделаю через try except'''

try:
    our_massiv = np.array([100, 200, 300], dtype='int8')
    print(our_massiv)
except OverflowError as e:
    print(e)


# Задача 3: Строки
# Преобразуй массив [10, 20, 30] в строки. Выведи.

mass_str = np.array([10, 20, 30], dtype='str_')
print(mass_str)


# Задача 4: Многомерные массивы
# Создай массив 3x3 с числами от 1 до 9. Выведи элемент [1, 2].

mass_3x3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mass_3x3[1, 2])
