import pandas as pd
import numpy as np

df = pd.DataFrame({
    'name': ['Ilya', 'Max', 'Alex', 'Dima', 'Ivan', 'Oleg'],
    'age': [19, 20, 21, 19, 22, 20],
    'score': [85, 92, 78, 64, 90, 71],
    'city': ['Moscow', 'Kazan', 'Moscow',
             'Sochi', 'Kazan', 'Moscow']
})


# Задача 1
# Создать Index со значениями A, B, A, C, D, C.
# Вывести уникальные значения, их количество,
# проверить уникальность и найти дубликаты.
# Преобразовать индекс в список Python и массив NumPy.

result_ind = pd.Index(['A', 'B', 'A', 'C', 'D', 'C'])
print(result_ind.unique())
print(result_ind.nunique())
print(result_ind.is_unique)
print(result_ind.duplicated())

to_list = result_ind.to_list()
to_numpy = result_ind.to_numpy()

print(type(to_list))
print(type(to_numpy))


# Задача 2
# Переименовать столбцы score -> grade и city -> location.
# Изменить стандартные индексы на student_0, student_1 и т.д.
# Изменения должны сохраниться в исходной таблице.

rename_index = pd.DataFrame({
    'name': ['Ilya', 'Max', 'Alex', 'Dima', 'Ivan', 'Oleg'],
    'age': [19, 20, 21, 19, 22, 20],
    'score': [85, 92, 78, 64, 90, 71],
    'city': ['Moscow', 'Kazan', 'Moscow',
             'Sochi', 'Kazan', 'Moscow']
})

rename_index.rename(
    columns={'score': 'grade', 'city': 'location'},
    inplace=True
)

rename_index.index = [
    'student_0', 'student_1', 'student_2',
    'student_3', 'student_4', 'student_5'
]

print(rename_index)


# Задача 3
# Сделать name индексом таблицы.
# Вывести данные студента Alex через loc.
# Вернуть name в обычный столбец.
# Создать составной индекс из city и name.
# Вернуть оба уровня индекса обратно в столбцы.

df.set_index('name', inplace=True)
print(df.loc['Alex'])

df.reset_index(inplace=True)

df.set_index(['city', 'name'], inplace=True)
print(df)

df.reset_index(inplace=True)
print(df)


# Задача 4
# Вывести студентов с оценкой больше 80.
# Вывести студентов, которым ровно 19 лет.
# Изменить все оценки меньше 75 на 75.

print(df.loc[df['score'] > 80])
print(df.loc[df['age'] == 19, 'name'])

df.loc[df['score'] < 75, 'score'] = 75
print(df)


# Задача 5
# Добавить столбец passed со значением False.
# Поставить True студентам с оценкой >= 80.
# Создать Series с индексами 0, 2, 4 и значениями 5, 10, 15.
# Добавить её в столбец bonus.
# Объяснить появление NaN и удалить bonus.

df['passed'] = False
df.loc[df['score'] >= 80, 'passed'] = True

series_bonus = pd.Series(
    [5, 10, 15],
    index=[0, 2, 4]
)

df['bonus'] = series_bonus
print(df)

# Значения сопоставляются по индексам.
# В строках 0, 2, 4 появляются 5.0, 10.0, 15.0.
# В остальных строках NaN, так как значений для них нет.

del df['bonus']
print(df)


# Задача 6
# Переименовать score в grade.
# Создать столбец result:
# Pass, если grade >= 75, иначе Fail.
# Создать составной индекс city + name.
# Вывести студентов Москвы через loc.
# Вернуть индексы в столбцы и вывести результат.

df = pd.DataFrame({
    'name': ['Ilya', 'Max', 'Alex', 'Dima', 'Ivan', 'Oleg'],
    'age': [19, 20, 21, 19, 22, 20],
    'score': [85, 92, 78, 64, 90, 71],
    'city': ['Moscow', 'Kazan', 'Moscow',
             'Sochi', 'Kazan', 'Moscow']
})

new_df = df.rename(columns={'score': 'grade'})
new_df['result'] = 'Fail'
new_df.loc[new_df['grade'] >= 75, 'result'] = 'Pass'

new_df.set_index(['city', 'name'], inplace=True)
print(new_df.loc['Moscow'])

new_df.reset_index(inplace=True)
print(new_df)
