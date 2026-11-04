import pandas as pd

df = pd.DataFrame({
    'name': ['Ilya', 'Max', 'Alex', 'Dima'],
    'math': [90, 65, 80, 40],
    'english': [75, 85, 95, 60]
})


# Задача 1
# Через DataFrame.apply() вычислить средний балл
# по математике и английскому.
# Создать столбец average.

def calculate_average(row):
    return (row['math'] + row['english']) / 2


# Первоначальное решение:
print(df.apply(calculate_average, axis=1), '\n')

# Доработка: сохраняем результат в столбец.
df['average'] = df.apply(calculate_average, axis=1)


# Задача 2
# Через Series.apply() увеличить оценку
# по математике на 5 баллов.
# Использовать дополнительный аргумент.

def add_points(score, bonus):
    return score + bonus


df['math_bonus'] = df['math'].apply(
    add_points,
    args=(5,)
)  # Также можно использовать bonus=5.

print(df['math_bonus'], '\n')


# Задача 3
# Создать столбец result:
# Pass — math >= 60 и english >= 70.
# Fail — в остальных случаях.
# Использовать DataFrame.apply().

def get_result(row):
    if row['math'] >= 60 and row['english'] >= 70:
        return 'Pass'
    return 'Fail'


df['result'] = df.apply(get_result, axis=1)

print(df['result'], '\n')


# Итоговая таблица
print(df)
