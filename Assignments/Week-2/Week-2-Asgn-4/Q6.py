"""
Q6. Don’t create a function, just print the following pattern 1  11  111  1111  11111....n times (Ask n from user)
"""


def pattern(n):
    i = 1
    res = 1
    while i <= n:
        print(res, end=" ")
        res = (res * 10) + 1
        i = i + 1
    print()


num: int = int(input("Enter a number: "))
pattern(num)
