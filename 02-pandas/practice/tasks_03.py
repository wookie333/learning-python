import pandas as pd

# Задача 1
# Прочитать файл students.csv и вывести только первые две строки,
# используя параметр nrows.

df = pd.read_csv('students.csv',
                 nrows=2)
print(df, '\n')


# Задача 2
# Прочитать students.csv и сделать столбец name индексом таблицы.

df = pd.read_csv('students.csv',
                 index_col=['name'])
print(df, '\n')


# Задача 3
# Прочитать только столбцы name и score.
# Затем извлечь score в отдельную Series.
# Проверить типы полученных объектов.

df = pd.read_csv('students.csv',
                 usecols=['name', 'score'])
score = df['score']
print(type(df))
print(type(score))


# Задача 4
# Прочитать students.csv так, чтобы столбец score имел тип float64.
# Вывести типы всех столбцов.

df = pd.read_csv('students.csv',
                 dtype={'score': 'float64'})
print(df.dtypes)


# Задача 5
# Прочитать исходную таблицу и сохранить её в students_result.csv.
# Условия:
# - сохранить только name и score;
# - использовать разделитель ;
# - не сохранять индексы;
# - сохранить названия столбцов.
# После сохранения прочитать полученный файл.

df = pd.read_csv('students.csv')
df.to_csv('students_result.csv',
          columns=['name', 'score'],
          sep=';',
          index=False,
          header=True)

result = pd.read_csv('students_result.csv', sep=';')
print(result)
