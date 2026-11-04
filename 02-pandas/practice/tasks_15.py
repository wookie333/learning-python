import pandas as pd

df = pd.DataFrame({
    'name': ['Ilya', 'Max', 'Alex', 'Dima'],
    'math': [90, 65, 80, 40],
    'english': [75, 85, 95, 60]
})


# Задача 1
# Одним вызовом agg() найти минимум,
# среднее и максимум для math и english.

print(df.agg({
    'math': ['min', 'mean', 'max'],
    'english': ['min', 'mean', 'max']
}), '\n')


# Задача 2
# Через словарь в agg() найти:
# - сумму оценок по math;
# - среднюю оценку по english.

print(df.agg({
    'math': 'sum',
    'english': 'mean'
}), '\n')


# Задача 3
# Найти min, mean, max только для math.
# Результат должен быть Series.

# Первоначально использовал словарь:
# df.agg({'math': ['min', 'mean', 'max']})
# Это возвращает DataFrame.

# Исправленное решение:
print(df['math'].agg(['min', 'mean', 'max']), '\n')


# Дополнительная проверка типов

print(type(df.agg({
    'math': ['min', 'mean', 'max']
})))

print(type(df['math'].agg(
    ['min', 'mean', 'max']
)))
