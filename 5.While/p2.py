# 1 2 4 8 16 64... upto N times


def pattern_1(n: int):
    i = 1
    res = 1
    while i <= n:
        print(res, end=" ")
        res = res * 2
        i += 1
    print()


pattern_1(10)

# ALTERNATE WAY:


def pattern_2(n: int):
    start = 1
    while start <= n:
        total = 2 ** (start - 1)
        print(total, end=" ")
        start += 1


pattern_2(10)
