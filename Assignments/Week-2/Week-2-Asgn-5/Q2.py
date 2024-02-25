"""
Q2. Write a program to display the n terms of a harmonic series and their sum.
    1 + 1/2 + 1/3 + 1/4 + 1/5 ... 1/n termsLets suppose n=5.
    1/1 + 1/2 + 1/3 + 1/4 + 1/5 = 2.283334
"""


def harmonic(n: int):
    i = 1
    sum: float = 0.0
    while i <= n:
        sum += 1 / i
        i += 1
    print()
    return sum


print(harmonic(5))


def harmonic_f(n: int):
    i = 1
    sum: float = 0.0
    for i in range(1, n):
        sum += 1 / i
        i += 1
    print()
    return sum


print(harmonic_f(5))
