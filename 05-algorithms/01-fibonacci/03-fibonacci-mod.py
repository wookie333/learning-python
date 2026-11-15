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
