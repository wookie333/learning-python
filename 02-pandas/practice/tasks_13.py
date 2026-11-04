import pandas as pd
import numpy as np

dict_array = {
    'age': [53, 53, 11, 18, 18, np.nan],
    'name': ['Сергей', 'Сергей', 'Ксюша', 'Аристарх', 'Соня', 'Соня'],
    'has car': [True, True, False, True, False, True]
}
df = pd.DataFrame(
    dict_array,
    index=['row_0', 'row_1', 'row_2', 'row_3', 'row_4', 'row_5']
)


# Задача 1
# Вывести уникальные имена и отдельно их количество.

print(df['name'].unique(), df['name'].nunique(), '\n')


# Задача 2
# Посчитать, какую долю составляет каждый возраст, включая пропуск.
# Вывести доли, а не проценты.

print(df['age'].value_counts(normalize=True, dropna=False), '\n')


# Задача 3
# Создать sorted_df: отсортировать людей по возрасту по убыванию.
# Пропуски разместить в конце.
# Исходный df должен остаться без изменений.

sorted_df = df.sort_values('age', ascending=False, na_position='last')
print(sorted_df)
