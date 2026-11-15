def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == "__main__":
    main()
