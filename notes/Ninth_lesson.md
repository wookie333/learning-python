# NumPy: булевы операции, inf и nan

## 1. Сравнение элементов

Операции сравнения выполняются поэлементно и возвращают массив из `True` и `False`.

```python
import numpy as np

a = np.array([1, 2, 3, 10, 20, 30])

print(a > 5)
# [False False False  True  True  True]

print(a[a > 5])
# [10 20 30]
```

Первый вариант возвращает булеву маску, второй выбирает элементы, для которых условие истинно.

### Функции сравнения

```python
a = np.array([1, 2, 3, 10, 20, 30])
b = np.array([1, 2, 3, 4, 5, 6])

print(a != b)           # Не равны
print(np.greater(a, b)) # a > b
print(np.less(a, b))    # a < b
print(np.equal(a, b))   # a == b
```

Эти функции возвращают булевы массивы.

## 2. Сравнение массивов целиком

`np.array_equal()` проверяет, совпадают ли массивы по форме и значениям.

```python
a = np.array([1, 2, 3])
b = np.array([1, 2, 3])
c = np.array([1, 2, 4])

print(np.array_equal(a, b))  # True
print(np.array_equal(a, c))  # False
```

## 3. Функции any() и all()

- `np.any()` возвращает `True`, если хотя бы один элемент удовлетворяет условию.
- `np.all()` возвращает `True`, только если условию удовлетворяют все элементы.

```python
a = np.array([1, 2, 3, 10, 20, 30])

print(np.any(a > 5))  # True
print(np.all(a > 0))  # True
print(np.all(a > 5))  # False
```

## 4. Значения inf и nan

В NumPy встречаются специальные значения:

- `np.inf` — положительная бесконечность.
- `-np.inf` — отрицательная бесконечность.
- `np.nan` — значение, обозначающее отсутствие корректного числового результата.

```python
a = np.array([1, 2, np.nan])

print(a.sum())
# nan
```

Обычное суммирование возвращает `nan`, если массив содержит `nan`.

Если нужно просуммировать остальные значения, можно использовать `np.nansum()`:

```python
print(np.nansum(a))
# 3.0
```

## 5. Проверка специальных значений

### isinf() и isnan()

```python
a = np.array([1, 2, np.nan, np.inf, -np.inf])

print(np.isinf(a))
# [False False False  True  True]

print(np.isnan(a))
# [False False  True False False]
```

Можно использовать маску, чтобы убрать бесконечности:

```python
mask = np.isinf(a)
print(a[~mask])
# [ 1.  2. nan]
```

`~` инвертирует булеву маску: `True` становится `False` и наоборот.

### isfinite()

`np.isfinite()` возвращает `True` для конечных чисел и `False` для `inf`, `-inf` и `nan`.

```python
print(np.isfinite(a))
# [ True  True False False False]
```

Например, чтобы оставить только конечные значения:

```python
print(a[np.isfinite(a)])
# [1. 2.]
```

## 6. Комплексные и действительные числа

```python
a = np.array([1 + 2j, 3 + 4j, 5])

print(np.iscomplex(a))
# [ True  True False]

print(np.isreal(a))
# [False False  True]
```

- `np.iscomplex()` проверяет, отлична ли мнимая часть от нуля.
- `np.isreal()` проверяет, равна ли мнимая часть нулю.

## 7. Логические операции

Логические функции работают с булевыми значениями.

```python
x = np.array([True, False, True, False])
y = np.array([True, True, False, False])

print(np.logical_and(x, y))
# [ True False False False]

print(np.logical_or(x, y))
# [ True  True  True False]

print(np.logical_not(x))
# [False  True False  True]

print(np.logical_xor(x, y))
# [False  True  True False]
```

| Функция | Значение |
|---|---|
| `np.logical_and(x, y)` | `True`, если оба значения истинны |
| `np.logical_or(x, y)` | `True`, если хотя бы одно значение истинно |
| `np.logical_not(x)` | Инвертирует значения |
| `np.logical_xor(x, y)` | `True`, если значения различаются |

## Что запомнить

| Функция | Назначение |
|---|---|
| `np.greater()` | Проверка `>` |
| `np.less()` | Проверка `<` |
| `np.equal()` | Проверка `==` |
| `np.array_equal()` | Сравнение массивов целиком |
| `np.any()` | Хотя бы один элемент удовлетворяет условию |
| `np.all()` | Все элементы удовлетворяют условию |
| `np.isnan()` | Поиск `nan` |
| `np.isinf()` | Поиск бесконечностей |
| `np.isfinite()` | Поиск конечных значений |
| `np.iscomplex()` | Проверка ненулевой мнимой части |
| `np.isreal()` | Проверка нулевой мнимой части |

Эти функции полезны для фильтрации данных, проверки условий и поиска некорректных значений перед анализом или обучением ML-моделей.
