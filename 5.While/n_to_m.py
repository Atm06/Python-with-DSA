"""
Ask M and N from user.
Print M to N using while.
"""


def m_to_n(m: int, n: int) -> None:
    i: int = m
    while i <= n:
        print(i, end=" ")
        i += 1


m: int = int(input("Enter M: "))
n: int = int(input("Enter N: "))
m_to_n(m, n)
