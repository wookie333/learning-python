import pandas as pd

df = pd.DataFrame({
    'name': ['Сергей', 'Маша', 'Ксюша', 'Аристарх', 'Соня'],
    'age': [53, 37, 11, 18, 7],
    'has car': [True, True, False, True, False]
}, index=['row_0', 'row_1', 'row_2', 'row_3', 'row_4'])


# Задача 1
# Через iloc вывести строки с позициями 1, 2 и 3.
# Выбрать только столбцы name и age.
# Результат должен быть DataFrame.

print(df.iloc[1:4, 0:2])
print(type(df.iloc[1:4, 0:2]), '\n')


# Задача 2
# Через loc вывести людей, у которых:
# - возраст больше 20 лет;
# - есть машина.
# Оставить только name и age.

print(df.loc[
    (df['age'] > 20) & (df['has car'] == True),
    ['name', 'age']
])

print(df, '\n')


# Задача 3
# Через at изменить возраст Ксюши на 15.
# Через iat изменить возраст Сони на 10.

df.at['row_2', 'age'] = 15
print(df, '\n\n')

df.iat[4, 1] = 10
print(df, '\n\n')


# Задача 4 — закрепление фильтрации
# Использовать исходный DataFrame.
# Через loc вывести только имена людей:
# - младше 20 лет;
# - без автомобиля.

df = pd.DataFrame({
    'name': ['Сергей', 'Маша', 'Ксюша', 'Аристарх', 'Соня'],
    'age': [53, 37, 11, 18, 7],
    'has car': [True, True, False, True, False]
}, index=['row_0', 'row_1', 'row_2', 'row_3', 'row_4'])

print(df.loc[
    (df['age'] < 20) & (df['has car'] == False),
    ['name']
])

# Ожидаемый результат: Ксюша и Соня.
