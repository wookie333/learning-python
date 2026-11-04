import pandas as pd

df = pd.DataFrame({
    'city': ['Moscow', 'Kazan', 'Moscow', 'Kazan', 'Moscow', 'Sochi'],
    'category': ['Books', 'Books', 'Tech', 'Tech', 'Books', 'Books'],
    'revenue': [1000, 500, 2000, 900, 3000, 700],
    'items': [2, 1, 4, 2, 3, 1]
})


# Задача 1
# Найти среднюю выручку для каждого города.
# Использовать groupby().

print(df.groupby('city')['revenue'].mean(), '\n')


# Задача 2
# Для каждого города найти минимальную,
# максимальную и суммарную выручку.
# Использовать groupby() и agg().

print(df.groupby('city')['revenue'].agg(
    ['min', 'max', 'sum']
), '\n')


# Задача 3
# Сгруппировать данные по city и category.
# Посчитать суммарное количество товаров items
# для каждой комбинации.

print(df.groupby(
    ['city', 'category']
)['items'].sum(), '\n')


# Задача 4
# Создать таблицу с колонками:
# city — название города;
# total_revenue — суммарная выручка;
# average_revenue — средняя выручка;
# sales_count — число продаж.
#
# Использовать именованные агрегации.
# city должен остаться обычным столбцом.

result = df.groupby('city', as_index=False).agg(
    total_revenue=('revenue', 'sum'),
    average_revenue=('revenue', 'mean'),
    sales_count=('revenue', 'size')
)

print(result, '\n')
