# Pandas — урок 13. unique(), nunique(), value_counts(), sort_values()

## 1. Исходные данные

```python
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
```

В таблице шесть строк. Первые две совпадают по всем значениям,
а в последней строке возраст неизвестен.

## 2. unique() — какие значения встречаются

```python
print(df['age'].unique())
# [53. 11. 18. nan]

print(df['name'].unique())
# ['Сергей' 'Ксюша' 'Аристарх' 'Соня']
```

Метод возвращает уникальные значения в порядке первого появления.
Он не сортирует их и сохраняет пропуск среди результатов.

Метод unique() есть у Series и Index, но не у DataFrame.
Для обычного числового Series, как age в примере, результат — массив NumPy.
Для некоторых других типов данных результат может быть ExtensionArray.

## 3. nunique() — сколько разных значений

```python
print(df['age'].nunique())              # 3
print(df['age'].nunique(dropna=False))  # 4
```

По умолчанию dropna=True: пропуски не учитываются.
В первом случае считаются 53, 11 и 18.
При dropna=False пропуск тоже учитывается как отдельный вариант.

Для DataFrame метод по умолчанию считает уникальные значения
отдельно в каждом столбце и возвращает Series:

```python
print(df.nunique())
# age        3
# name       4
# has car    2
```

Важно различать: unique() возвращает сами значения,
а nunique() — их количество.

## 4. value_counts() — сколько раз встречается значение

Для Series:

```python
print(df['has car'].value_counts())
# True     4
# False    2
```

Результат — Series: значения находятся в индексе,
а рядом указано количество повторений.
По умолчанию результат отсортирован по частоте по убыванию.

Для DataFrame считаются сочетания значений в строках:

```python
print(df.value_counts())
```

Сочетание age=53, name='Сергей', has car=True встретится дважды.
Метки row_0 и row_1 не мешают этому: индекс строк в сравнении не участвует.
По умолчанию строка с пропуском в учитываемых столбцах исключается.

Можно выбрать только нужные столбцы:

```python
print(df.value_counts(['age', 'name']))
```

Теперь считаются пары «возраст + имя», а has car не участвует.
Чтобы включить пары с пропущенным возрастом:

```python
print(df.value_counts(['age', 'name'], dropna=False))
```

## 5. normalize=True — доли вместо количества

```python
print(df.value_counts('name', normalize=True))
```

Каждое количество делится на общее число учитываемых строк:

| Имя | Количество | Доля |
|---|---:|---:|
| Сергей | 2 | 2 / 6 ≈ 0.3333 |
| Соня | 2 | 2 / 6 ≈ 0.3333 |
| Ксюша | 1 | 1 / 6 ≈ 0.1667 |
| Аристарх | 1 | 1 / 6 ≈ 0.1667 |

Сумма долей равна 1 с учётом погрешности вычислений.
Для процентов умножаем результат на 100:

```python
print(df.value_counts('name', normalize=True) * 100)
```

Доля 0.3333 означает примерно 33.33%.
normalize=True меняет форму результата подсчёта, но не исходный df.

### Пропуски меняют знаменатель

```python
print(df['age'].value_counts(normalize=True))
# 53.0 и 18.0 — по 2/5 = 0.4
# 11.0 — 1/5 = 0.2
```

Пропущенный возраст исключён: учитываются пять строк.

```python
print(df['age'].value_counts(normalize=True, dropna=False))
# 53.0 и 18.0 — по 2/6 ≈ 0.3333
# 11.0 и NaN — по 1/6 ≈ 0.1667
```

Теперь учитываются все шесть строк.
Если считать только по name, пропуск в age не влияет на подсчёт:
в name пропусков нет, поэтому обе строки с Соней учитываются.

## 6. sort_values() — сортировка по значениям

```python
print(df.sort_values('age'))
```

По умолчанию ascending=True: возраст сортируется по возрастанию.
Получим последовательность 11, 18, 18, 53, 53, NaN.

По убыванию:

```python
print(df.sort_values('age', ascending=False))
```

Получим 53, 53, 18, 18, 11, NaN.
Строки перемещаются целиком, вместе с именами, наличием автомобиля и индексами.
Сортировка сама по себе не перенумеровывает индексы.
Для строк с одинаковым возрастом здесь не задаём дополнительный порядок.

### Положение пропусков

```python
print(df.sort_values('age', na_position='first'))
print(df.sort_values('age', na_position='last'))
```

- first — пропуски в начале.
- last — пропуски в конце, это значение по умолчанию.

na_position действует независимо от ascending.
Например, при ascending=False и na_position='first'
первой будет row_5 с пропущенным возрастом, затем — известные возраста по убыванию.

## 7. Новый DataFrame и inplace=True

Чтобы сохранить исходную таблицу и получить отдельный результат:

```python
sorted_df = df.sort_values('age', ascending=False, na_position='last')
print(sorted_df)
```

Чтобы изменить сам df:

```python
df.sort_values('age', na_position='last', inplace=True)
print(df)
```

С inplace=True метод возвращает None.
Поэтому такой вызов напечатает None, хотя таблица будет отсортирована:

```python
print(df.sort_values('age', inplace=True))
```

Не нужно присваивать результат вызова с inplace=True обратно в df:
вместо таблицы переменная получит None.

## 8. Проверка понимания

- Доли has car: True — 4/6, False — 2/6.
- Число уникальных возрастов: 3 без пропуска, 4 с пропуском.
- При na_position='first' первой будет строка с NaN даже при сортировке по убыванию.
- Доли и проценты отличаются множителем 100.

Практика: [tasks_13.py](../practice/tasks_13.py).

## Главное из урока

| Метод / параметр | Что делает |
|---|---|
| unique() | Возвращает уникальные значения |
| nunique() | Считает количество уникальных значений |
| value_counts() | Считает частоты значений или сочетаний |
| normalize=True | Возвращает доли вместо количества |
| dropna=False | Включает пропуски в подсчёт |
| sort_values() | Сортирует по значениям |
| ascending=False | Задаёт порядок по убыванию |
| na_position | Управляет положением пропусков |
| inplace=True | Изменяет исходную таблицу и возвращает None |

## Справка

- [Series.unique](https://pandas.pydata.org/docs/reference/api/pandas.Series.unique.html)
- [DataFrame.nunique](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nunique.html)
- [DataFrame.value_counts](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html)
- [DataFrame.sort_values](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html)
