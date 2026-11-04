import pandas as pd

df1 = pd.DataFrame({
    'name': ['Ilya', 'Max'],
    'score': [90, 80]
})

df2 = pd.DataFrame({
    'name': ['Alex', 'Dima'],
    'score': [75, 95]
})

users = pd.DataFrame({
    'user_id': [1, 2, 3],
    'name': ['Ilya', 'Max', 'Alex']
})

cities = pd.DataFrame({
    'user_id': [1, 3, 4],
    'city': ['Moscow', 'Kazan', 'Sochi']
})


# Задача 1
# Объединить df1 и df2 по строкам.
# Индексы должны быть 0, 1, 2, 3.

print(pd.concat([df1, df2], ignore_index=True), '\n')


# Задача 2
# Объединить users и cities.
# Оставить только совпадающие user_id.

print(users.merge(
    cities,
    on='user_id',
    how='inner'
), '\n')


# Задача 3
# Сохранить всех пользователей из users.
# Если город неизвестен, оставить NaN.

result = users.merge(
    cities,
    on='user_id',
    how='left'
)

print(result, '\n')


# Задача 4
# Сохранить все ключи обеих таблиц.
# Добавить столбец с происхождением строк.

print(users.merge(
    cities,
    on='user_id',
    how='outer',
    indicator=True
), '\n')


# Вывод:
# inner оставляет только совпадающие ключи.
# left сохраняет все строки левой таблицы.
# outer сохраняет ключи обеих таблиц.
#
# NaN появляется там, где не нашлось
# соответствующей строки из другой таблицы.
