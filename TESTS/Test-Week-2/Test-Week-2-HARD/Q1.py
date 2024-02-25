"""
Q1. Make a function named reverse which accepts an integer n from the
    user. Reverse the number passed as a parameter and return the reverse
    number. Do not use STRINGS
"""


def reverse(n: int) -> int:
    rev: int = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev
    print()


print(reverse(135))
print(reverse(1000))
print(reverse(1474))
