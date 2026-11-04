import pandas as pd

df = pd.DataFrame({
    'order_id': [101, 102, 103, 104, 105],
    'date': [
        '2026-10-25',
        '2026-10-28',
        '2026-11-01',
        '2026-11-03',
        '2026-11-05'
    ],
    'revenue': [1200, 2500, 800, 3100, 1700]
})


# Задача 1
# Преобразовать столбец date в тип даты.
# Вывести типы данных всех столбцов.

df['date'] = pd.to_datetime(df['date'])
print(df.dtypes)


# Задача 2
# Создать новые столбцы:
# month — номер месяца;
# weekday — номер дня недели (понедельник = 0).

df['month'] = df['date'].dt.month
df['weekday'] = df['date'].dt.dayofweek

print(df, '\n')


# Задача 3
# Через loc выбрать все заказы за ноябрь 2026 года.
# Использовать границы дат, а не только номер месяца.

result = df.loc[
    (df['date'] >= '2026-11-01') &
    (df['date'] < '2026-12-01')
]

print(result, '\n')

# Альтернативный вариант:
print(df.loc[df['date'].dt.month == 11], '\n')

# Важно: второй вариант выберет ноябрь
# за все годы, если в таблице их несколько.


# Задача 4
# Через groupby() и agg() вычислить
# общую и среднюю выручку по месяцам.
# Назвать столбцы total_revenue и average_revenue.

new_reslt = df.groupby('month').agg(
    total_revenue=('revenue', 'sum'),
    average_revenue=('revenue', 'mean')
)

print(new_reslt, '\n')


# Дополнительное наблюдение:
# Группировка только по номеру месяца объединяет
# данные за одинаковые месяцы разных лет.

# Для разделения по годам и месяцам:
result_by_period = df.groupby(
    df['date'].dt.to_period('M')
).agg(
    total_revenue=('revenue', 'sum'),
    average_revenue=('revenue', 'mean')
)

print(result_by_period)
