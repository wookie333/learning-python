"""
Задача 3. Огромное число Фибоначчи по модулю

Условие:
Даны два целых числа n и m. Необходимо найти
остаток от деления n-го числа Фибоначчи на m.

Ограничения:
1 <= n <= 10^18
2 <= m <= 10^5

Пример:
Ввод: 10 2
Вывод: 1

Идея:
Используем период Пизано — длину повторяющейся
последовательности остатков чисел Фибоначчи.

Сначала находим период, затем сокращаем
количество итераций с помощью n % period.

Сложность:
Время — O(m)
Память — O(1)
"""


def pisano_period(m):
    a, b = 0, 1
    count = 0

    while True:
        a, b = b, (a + b) % m
        count += 1

        if a == 0 and b == 1:
            return count


def fib_mod(n, m):
    period = pisano_period(m)
    n %= period

    a, b = 0, 1

    for i in range(n):
        a, b = b, (a + b) % m

    return a


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
