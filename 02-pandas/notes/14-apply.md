# Pandas — урок 14. Метод apply()

## 1. Что такое apply()?

apply() позволяет применить функцию к данным
Series или DataFrame.

Главное различие:

- DataFrame.apply() — обработка строк или столбцов.
- Series.apply() — обычно обработка каждого значения.

## 2. DataFrame.apply()

```python
import pandas as pd

df = pd.DataFrame({
    'math': [90, 65, 80],
    'english': [75, 85, 95]
})

def calculate_average(row):
    return (row['math'] + row['english']) / 2

df['average'] = df.apply(calculate_average, axis=1)
```

axis=0 — функция получает каждый столбец (по умолчанию).
axis=1 — функция получает каждую строку.

Функция может возвращать одно значение
или несколько значений.

## 3. Series.apply()

При стандартном использовании функция
получает отдельные элементы Series.

```python
def add_bonus(score):
    return score + 10

df['math_bonus'] = df['math'].apply(add_bonus)
```

Каждая оценка увеличивается на 10.

## 4. Дополнительные аргументы

Функции можно передавать дополнительные параметры.

```python
def add_points(score, bonus):
    return score + bonus
```

Через args:

```python
df['math'].apply(add_points, args=(5,))
```

Через именованный аргумент:

```python
df['math'].apply(add_points, bonus=5)
```

Оба варианта прибавляют 5 к каждому значению.

(5,) — кортеж из одного элемента.

## 5. raw=False и raw=True

Параметр raw относится к DataFrame.apply().

raw=False (по умолчанию):
- функция получает pandas Series;
- доступны метки индексов и атрибут name.

raw=True:
- функция получает NumPy ndarray;
- метки Pandas недоступны;
- иногда помогает ускорить числовые операции.

```python
import numpy as np

df.apply(np.mean, axis=0, raw=False)
df.apply(np.mean, axis=0, raw=True)
```

Для обычного числового DataFrame оба варианта
дают одинаковые средние значения.

raw=True не гарантирует ускорения.

## 6. Пользовательская функция с условием

```python
def get_result(row):
    if row['math'] >= 60 and row['english'] >= 70:
        return 'Pass'
    return 'Fail'

df['result'] = df.apply(get_result, axis=1)
```

Так можно создавать новые признаки
на основе существующих столбцов.

## 7. Замер скорости

```python
from time import perf_counter

start = perf_counter()
df.apply(np.sum, axis=0, raw=False)
finish = perf_counter()

print(round(finish - start, 3))
```

perf_counter() позволяет измерять
прошедшее время.

Для сравнения скорости нужно делать
несколько замеров, а не один.

## 8. Когда apply() лучше не использовать?

Если существует готовая векторизованная
операция Pandas или NumPy, обычно
лучше использовать её.

Вместо:

```python
df['math'].apply(add_bonus)
```

проще:

```python
df['math'] + 10
```

Вместо:

```python
df.apply(np.sum)
```

проще:

```python
df.sum()
```

Векторизованные операции обычно быстрее
и делают код более читаемым.

## 9. Что важно для ML?

apply() может использоваться для:
- обработки отдельных значений;
- создания новых признаков;
- преобразования строк;
- сложных пользовательских функций.

Но для больших датасетов стоит сначала
проверять возможность векторизации.

## Главное из урока

- apply(func) — применение функции к данным.
- DataFrame.apply(axis=0) — по столбцам.
- DataFrame.apply(axis=1) — по строкам.
- Series.apply() — обычно по отдельным значениям.
- args=(...) — дополнительные позиционные аргументы.
- bonus=5 — дополнительный именованный аргумент.
- raw=False — передаётся Series.
- raw=True — передаётся ndarray.
- Векторизация предпочтительнее, если она доступна.
