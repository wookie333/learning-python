# Pandas — урок 3. Чтение и запись CSV

## 1. Что такое CSV

CSV (Comma-Separated Values) — текстовый формат хранения табличных данных.

Пример файла students.csv:

```csv
name,age,score
Ilya,19,85
Max,20,92
Alex,21,78
```

Первая строка обычно содержит названия столбцов.
Остальные строки — данные.

CSV сам по себе не хранит типы данных Pandas. При чтении файла
Pandas пытается определить их автоматически.

## 2. Чтение CSV — read_csv()

```python
import pandas as pd

df = pd.read_csv('students.csv')
print(df)
```

read_csv() читает файл и возвращает DataFrame.

### sep — разделитель

По умолчанию используется запятая.

```python
df = pd.read_csv('students.csv', sep=';')
```

Если в файле разделитель `;`, а мы его не указали,
Pandas может прочитать всю строку как один столбец.

### usecols — выбор столбцов

```python
df = pd.read_csv(
    'students.csv',
    usecols=['name', 'score']
)
```

Загружаются только указанные столбцы.

### nrows — количество строк

```python
df = pd.read_csv('students.csv', nrows=2)
```

Читаются только две строки данных, без учёта заголовка.

Отличие от head():

```python
df = pd.read_csv('students.csv')
print(df.head(2))
```

head(2) показывает две строки уже загруженного DataFrame.
А nrows=2 ограничивает чтение самого файла.

Для предварительного просмотра большого CSV nrows часто удобнее.

### index_col — выбор индекса

```python
df = pd.read_csv(
    'students.csv',
    index_col='name'
)
```

Теперь name используется как индекс вместо стандартных 0, 1, 2.

Можно обратиться к строке:

```python
print(df.loc['Ilya'])
```

Если одновременно используем usecols и index_col,
столбец индекса должен входить в usecols:

```python
df = pd.read_csv(
    'students.csv',
    usecols=['name', 'score'],
    index_col='name'
)
```

### dtype — типы данных

```python
df = pd.read_csv(
    'students.csv',
    dtype={'score': 'float64'}
)
```

Типы задаются словарём: название столбца -> нужный тип.

Примеры типов:
- int64 — целые числа
- float64 — вещественные числа
- str — строки
- category — категориальные значения

category может экономить память, если в столбце много
повторяющихся значений, например названий городов.

Посмотреть типы:

```python
print(df.dtypes)
```

Посмотреть общую информацию:

```python
df.info()
```

info() уже выводит информацию самостоятельно.
Писать print(df.info()) не нужно: дополнительно появится None.

## 3. DataFrame и Series

Даже при выборе одного столбца read_csv() возвращает DataFrame:

```python
df = pd.read_csv(
    'students.csv',
    usecols=['name']
)
```

Чтобы получить Series:

```python
names = df['name']
```

Разница:

```python
df['name']     # Series
df[['name']]   # DataFrame
```

Переменная names не обязательна — она просто хранит Series.

В старых уроках встречается параметр squeeze=True.
В современных версиях Pandas он удалён.

## 4. Работа с датами — parse_dates

Пример users.csv:

```csv
name,registration_date
Ilya,2026-10-10
Max,2026-10-15
Alex,2026-10-19
```

Без parse_dates даты обычно читаются как строки:

```python
df = pd.read_csv('users.csv')
```

С parse_dates Pandas пытается преобразовать их в datetime:

```python
df = pd.read_csv(
    'users.csv',
    parse_dates=['registration_date']
)
```

Внешне таблица почти не меняется, но тип данных становится другим.

Теперь с датами можно выполнять вычисления:

```python
difference = (
    df.loc[1, 'registration_date']
    - df.loc[0, 'registration_date']
)

print(difference)
```

Результат: разница в 5 дней.

Можно преобразовать даты после загрузки:

```python
df = pd.read_csv('users.csv')

df['registration_date'] = pd.to_datetime(
    df['registration_date']
)
```

Если год, месяц и день хранятся отдельно:

```python
df['registration_date'] = pd.to_datetime(
    df[['year', 'month', 'day']]
)
```

Важно: преобразование в DataFrame не изменяет исходный CSV.

## 5. encoding — кодировка

```python
df = pd.read_csv(
    'students.csv',
    encoding='utf-8'
)
```

Кодировка определяет, как байты файла превращаются в символы.

UTF-8 обычно используется по умолчанию.
Параметр особенно полезен при проблемах с русским текстом.

## 6. Запись CSV — to_csv()

read_csv() — файл -> DataFrame.
to_csv() — DataFrame -> файл.

Пример:

```python
df.to_csv('students_result.csv')
```

По умолчанию сохраняются и индексы DataFrame.

### index

```python
df.to_csv('students_result.csv', index=False)
```

index=False не удаляет индексы из DataFrame.
Он только запрещает записывать их в CSV.

index=True сохраняет существующие индексы.
Они необязательно начинаются с нуля.

### columns

```python
df.to_csv(
    'students_result.csv',
    columns=['name', 'score'],
    index=False
)
```

Сохраняются только выбранные столбцы.

### sep

```python
df.to_csv(
    'students_result.csv',
    sep=';',
    index=False
)
```

Если сохранили файл с `sep=';'`, при повторном чтении
тоже нужно указать этот разделитель:

```python
result = pd.read_csv('students_result.csv', sep=';')
```

### header

```python
df.to_csv(
    'students_result.csv',
    header=False,
    index=False
)
```

header=False — не сохранять названия столбцов.
По умолчанию header=True.

### index_label

```python
df.to_csv(
    'students_result.csv',
    index=True,
    index_label='student_id'
)
```

index_label задаёт название столбца индексов в CSV.

### Перезапись файла

По умолчанию to_csv() перезаписывает существующий файл.

Поэтому лучше не сохранять результат поверх исходных данных:

```python
df = pd.read_csv('students.csv')
df.to_csv('students_result.csv', index=False)
```

## 7. Пути к файлам

Относительный путь:

```python
pd.read_csv('students.csv')
```

Он считается от текущей рабочей директории процесса,
а не обязательно от папки, где находится Python-скрипт.

Проверить рабочую директорию:

```python
import os
print(os.getcwd())
```

Абсолютный путь указывает полное расположение файла.

Если нужно искать CSV относительно самого скрипта:

```python
from pathlib import Path

file_path = Path(__file__).resolve().parent / 'students.csv'
df = pd.read_csv(file_path)
```

FileNotFoundError обычно означает, что файл не найден
по указанному пути. Стоит проверить название, расширение
и рабочую директорию.

## 8. SQLite

Pandas умеет читать данные не только из CSV,
но и из баз данных.

Например, для SQLite существуют read_sql() и to_sql().

Подробно разберу это позже, во время изучения SQL.

## Главное

Основные параметры read_csv():
- sep
- usecols
- nrows
- index_col
- dtype
- parse_dates
- encoding

Основные параметры to_csv():
- sep
- columns
- index
- header
- index_label

Главная идея: сначала правильно загрузить данные,
проверить их структуру и типы, затем сохранить результат
в нужном формате.
