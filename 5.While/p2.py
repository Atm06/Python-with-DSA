# 1 2 4 8 16 64... upto N times


def pattern(n: int):
    i = 1
    res = 1
    while i <= n:
        print(res, end=" ")
        res = res * 2
        i += 1


pattern(10)
