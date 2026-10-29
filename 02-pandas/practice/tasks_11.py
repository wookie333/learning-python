import pandas as pd
import numpy as np

df = pd.DataFrame({
    'name': ['Ilya', 'Max', 'Alex', 'Dima'],
    'age': [19, 20, 21, 22],
    'score': [85.0, 92.0, 78.0, 64.0],
    'city': ['Moscow', 'Kazan', 'Moscow', 'Kazan']
})


# Задача 1
# Удалить строку с индексом 1 и столбец age
# одним вызовом drop().
# Исходный DataFrame не должен измениться.

print(df.drop(index=1, columns='age'), '\n')


# Задача 2
# Создать новый DataFrame new_df.
# Преобразовать score в int32, а city в category.
# Остальные типы данных не изменять.
# Вывести типы столбцов.

new_df = df.astype({
    'score': np.int32,
    'city': 'category'
})

print(new_df.dtypes, '\n')


# Задача 3
# Сравнить расход памяти исходного df
# и преобразованного new_df.
# Объяснить, почему он изменился.

print(df.memory_usage(), '\n')
print(new_df.memory_usage(), '\n')


# Дополнительное сравнение
# deep=True позволяет точнее оценить память,
# занятую строковыми значениями.

print(df.memory_usage(deep=True), '\n')
print(new_df.memory_usage(deep=True), '\n')


# Вывод:
# score: float64 -> int32.
# Один элемент стал занимать 4 байта вместо 8.
#
# city: строковый тип -> category.
# Pandas хранит категории и их числовые коды.
# На больших таблицах с повторяющимися значениями
# это часто помогает экономить память.
#
# Но здесь всего четыре строки, поэтому category
# может занимать больше памяти из-за дополнительных
# затрат на хранение категорий.
