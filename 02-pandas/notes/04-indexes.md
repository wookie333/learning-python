# Pandas — урок 4. Индексы строк и столбцов

## 1. Что такое Index

Index — объект Pandas, который хранит метки строк или столбцов.

Индексы не обязательно должны быть числами 0, 1, 2.
Они могут быть строками, датами и другими значениями.

```python
import pandas as pd
import numpy as np

index_data = pd.Index(['A', 'B', 'A', 'C'], name='rows')
print(index_data)
```

В индексе могут встречаться повторяющиеся метки.

У DataFrame есть два основных свойства:

```python
df.index     # Индексы строк
df.columns   # Метки столбцов
```

Пример:

```python
df = pd.DataFrame(
    {'score': [85, 92, 78]},
    index=['Ilya', 'Max', 'Alex']
)
```

Здесь Ilya, Max, Alex — метки строк.

## 2. to_list() и to_numpy()

Индекс Pandas можно преобразовать в другие структуры данных.

```python
index_data = pd.Index(['Ilya', 'Max', 'Alex'])

names_list = index_data.to_list()
names_array = index_data.to_numpy()

print(type(names_list))   # list
print(type(names_array))  # numpy.ndarray
```

to_list() возвращает обычный список Python.
to_numpy() возвращает массив NumPy.

Это полезно, если другой код ожидает конкретную структуру данных.

## 3. unique(), nunique(), is_unique(), duplicated()

Создадим индекс с повторениями:

```python
index_data = pd.Index(['A', 'B', 'A', 'C', 'D', 'C'])
```

### unique()

Возвращает уникальные значения индекса:

```python
print(index_data.unique())
```

Результат: A, B, C, D.

### nunique()

Возвращает количество уникальных значений:

```python
print(index_data.nunique())  # 4
```

### is_unique

Проверяет, уникальны ли все метки:

```python
print(index_data.is_unique)  # False
```

Это свойство, поэтому скобки не нужны.

### duplicated()

Возвращает булеву маску повторяющихся значений:

```python
print(index_data.duplicated())
```

Результат:

```text
[False False True False False True]
```

True означает, что значение уже встречалось раньше.

## 4. Название индекса

Индекс может иметь имя:

```python
index_data = pd.Index(['A', 'B'], name='rows')
print(index_data.name)
```

Имя можно изменить:

```python
index_data.name = 'students'
```

Важно различать имя всего индекса и сами метки индекса.

## 5. Метод rename()

rename() позволяет изменять названия столбцов или метки строк.

```python
df = pd.DataFrame({
    'name': ['Ilya', 'Max'],
    'score': [85, 92]
})
```

Переименование столбца:

```python
new_df = df.rename(columns={'score': 'grade'})
```

По умолчанию rename() возвращает новый DataFrame.
Исходный df при этом не изменяется.

Если хотим сохранить изменение в переменную:

```python
df = df.rename(columns={'score': 'grade'})
```

Или изменить существующий DataFrame:

```python
df.rename(columns={'score': 'grade'}, inplace=True)
```

### axis

axis=0 — метки строк.
axis=1 — метки столбцов.

Например:

```python
df.rename({'score': 'grade'}, axis=1, inplace=True)
```

### inplace=True

inplace=True означает, что метод изменяет существующий объект,
а не возвращает новую таблицу с изменениями.

При inplace=True метод rename() возвращает None.

Поэтому:

```python
print(df.rename(columns={'score': 'grade'}, inplace=True))
```

напечатает None, хотя df изменится.

Правильнее:

```python
df.rename(columns={'score': 'grade'}, inplace=True)
print(df)
```

## 6. Пропуски в индексах

Индекс может содержать отсутствующие значения.

```python
index_data = pd.Index([1, np.nan, 3, np.nan, 5])
```

### hasnans

```python
print(index_data.hasnans)
```

True означает, что есть хотя бы один пропуск.

### isna()

```python
print(index_data.isna())
```

Возвращает булеву маску пропусков:

```text
[False True False True False]
```

### dropna()

```python
print(index_data.dropna())
```

Возвращает новый индекс без пропущенных меток.

Важно: вызов dropna() у Index сам по себе не удаляет
строки из DataFrame.

## Главное из урока

- Index хранит метки строк и столбцов.
- Метки не обязаны быть уникальными.
- index и columns позволяют получить индексы DataFrame.
- unique() — уникальные значения.
- nunique() — количество уникальных значений.
- is_unique — проверка уникальности.
- duplicated() — маска повторений.
- rename() — переименование.
- inplace=True — изменение существующего объекта.
- hasnans, isna(), dropna() — работа с пропусками в индексах.
