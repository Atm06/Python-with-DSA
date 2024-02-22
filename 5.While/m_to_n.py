"""
Ask M from user
Ask N from user

M=5
N=10
o/p = 5 6 7 8 9 10

M = 9
N = 3
o/p = 3 4 5 6 7 8 9
"""

# Method- 1:


def m_to_n(m: int, n: int) -> None:
    if m <= n:
        i = m
        while i <= n:
            print(i, end=" ")
            i += 1
    else:
        i = n
        while i <= m:
            print(i, end=" ")
            i += 1


m: int = int(input("Enter value of m: "))
n: int = int(input("Enter value of n: "))
m_to_n(m, n)


# Method - 2
def M_to_N(M: int, N: int) -> None:
    if M <= N:
        i = M
        while i <= N:
            print(i, end=" ")
            i += 1


M: int = int(input("Enter value of M: "))
N: int = int(input("Enter value of N: "))

if M > N:
    M_to_N(N, M)
else:
    M_to_N(M, N)
