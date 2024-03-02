"""
        1
      2 2 2
    3 3 3 3 3
  4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5    
"""


def pattern(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end=" ")
        for k in range(2 * i - 1):
            print(i, end=" ")
        print()


pattern(5)
