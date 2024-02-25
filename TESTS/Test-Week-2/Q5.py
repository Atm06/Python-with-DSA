"""
Q5. Make a function named sumPattern that takes an integer n as an argument from the user.
    And then calculate the sum of the following pattern.
"""


def factorial(n: int) -> int:
    i = 1
    fact: int = 1
    while i <= n:
        fact *= i
        i += 1
    return fact


def sumPattern(n: int):
    sum: float = 0.0
    for i in range(1, n + 1):
        sum += 1 / factorial(i)
    return sum
    print()


print(sumPattern(5))
