"""
Just solve the following patterns using FOR / WHILE loop
Q1. 2  22  222  2222  22222 ... upto n. (Ask n from user)
"""

# Using While loop


def pattern_w(n: int):
    i = 1
    num: int = 2
    while i <= n:
        print(num, end=" ")
        num = (num * 10) + 2
        i += 1
    print()


pattern_w(10)

# Using For loop


def pattern_f(n: int):
    num: int = 2
    for i in range(1, n + 1):
        print(num, end=" ")
        num = (num * 10) + 2
        i += 1
    print()


pattern_f(10)
