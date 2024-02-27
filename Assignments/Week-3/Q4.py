"""
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
"""


def pattern(n: int):
    for i in range(1, n + 1):
        for j in range(5, 6 - i - 1, -1):
            print(j, end=" ")
        print()


pattern(5)
