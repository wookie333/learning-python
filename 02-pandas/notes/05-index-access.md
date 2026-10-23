# Pandas — урок 5. Индексы и доступ к данным

## 1. set_index()

set_index() позволяет сделать один или несколько столбцов
индексами DataFrame.

Пример:

```python
import pandas as pd

df = pd.DataFrame({
    'name': ['Ilya', 'Max', 'Alex'],
    'age': [19, 20, 21],
    'score': [85, 92, 78]
})
```

Сделаем name индексом:

```python
df.set_index('name', inplace=True)
print(df)
```

Получится:

```text
      age  score
name
Ilya   19     85
Max    20     92
Alex   21     78
```

По умолчанию name перестаёт быть обычным столбцом.

## 2. MultiIndex — составной индекс

Можно использовать несколько столбцов одновременно:

```python
df.set_index(['city', 'name'], inplace=True)
```

Получится индекс с двумя уровнями:
- city
- name

Такой индекс называется MultiIndex.

### append=True

```python
df.set_index(['city', 'name'], append=True)
```

Добавляет новые уровни к существующему индексу.

### append=False

```python
df.set_index(['city', 'name'], append=False)
```

Заменяет существующий индекс новыми уровнями.
Это поведение по умолчанию.

## 3. reset_index()

reset_index() превращает индексы обратно в обычные столбцы
и создаёт стандартный числовой индекс.

```python
df.reset_index(inplace=True)
```

Можно сбросить только один уровень составного индекса:

```python
df.reset_index(['city'], inplace=True)
```

Остальные уровни индекса сохранятся.

### Почему иногда выводится None?

```python
print(df.reset_index(inplace=True))
```

Выведет None.

Причина: метод изменяет сам df и ничего не возвращает.

Правильно:

```python
df.reset_index(inplace=True)
print(df)
```

## 4. Доступ к данным через loc

loc позволяет обращаться к строкам по меткам индекса.

```python
df = pd.DataFrame(
    {'score': [85, 92, 78]},
    index=['Ilya', 'Max', 'Alex']
)

print(df.loc['Alex'])
```

Если индекс состоит из city и name, можно выбрать город:

```python
df.set_index(['city', 'name'], inplace=True)
print(df.loc['Moscow'])
```

Здесь предполагается, что в DataFrame существуют
столбцы city и name.

loc использует метки, а не порядковые номера строк.

## 5. Добавление столбцов

Новый столбец можно создать присваиванием:

```python
df['passed'] = False
```

Во всех строках нового столбца будет False.

Можно добавить числовой столбец:

```python
df['bonus'] = 10
```

## 6. Выравнивание Series по индексам

Pandas сопоставляет значения Series с DataFrame
по меткам индексов.

```python
df = pd.DataFrame({
    'name': ['Ilya', 'Max', 'Alex', 'Dima', 'Ivan', 'Oleg']
})

bonus = pd.Series(
    [5, 10, 15],
    index=[0, 2, 4]
)

df['bonus'] = bonus
```

Значения появятся в строках с индексами 0, 2 и 4.

В остальных строках будут NaN, поскольку для их
индексов нет соответствующих значений в bonus.

Это не ошибка — так работает выравнивание данных.

## 7. Удаление столбцов

Столбец можно удалить через del:

```python
del df['bonus']
```

После этого столбца bonus в DataFrame не будет.

## 8. Булевы маски

Булева маска — последовательность значений True и False.

True — выбрать строку.
False — пропустить строку.

Например:

```python
df = pd.DataFrame({
    'name': ['Ilya', 'Max', 'Alex'],
    'score': [85, 92, 70]
})

print(df[df['score'] > 80])
```

Будут выбраны строки студентов с оценкой больше 80.

Через loc можно выбрать определённые столбцы:

```python
print(df.loc[df['score'] > 80, 'name'])
```

А можно изменить значения:

```python
df.loc[df['score'] < 75, 'score'] = 75
```

Теперь все оценки ниже 75 заменятся на 75.

### Условное заполнение нового столбца

```python
df['result'] = 'Fail'

df.loc[df['score'] >= 75, 'result'] = 'Pass'
```

Получится:
- Pass — оценка не меньше 75.
- Fail — оценка меньше 75.

Это полезно для обработки данных и создания
новых признаков в ML.

## 9. Обращение к столбцам

Обычный вариант:

```python
print(df['score'])
```

Иногда можно использовать:

```python
print(df.score)
```

Но запись через квадратные скобки надёжнее:
она работает и с пробелами в названиях столбцов.

Например:

```python
print(df['student score'])
```

## Главное из урока

- set_index() — сделать столбец индексом.
- reset_index() — вернуть индекс в столбцы.
- MultiIndex — индекс с несколькими уровнями.
- loc — доступ к данным по меткам.
- df['new'] = value — создать столбец.
- del df['column'] — удалить столбец.
- Булевы маски позволяют выбирать и изменять строки.
- При присваивании Series данные выравниваются по индексам.
