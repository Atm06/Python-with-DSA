"""
Create a function addDigits() that takes an integer as an argument. 
Calculate the sum of digits of that number.
"""


def addDigits(n: int) -> int:
    sum: int = 0
    for i in range(1, n + 1):
        sum += n % 10
        n = n // 10
    return sum


print(addDigits(104))
