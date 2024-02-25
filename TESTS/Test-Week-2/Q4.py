"""
Q4. Make a function named factorial(), which takes an integer n. Return the factorial of that number
"""


def factorial(n: int) -> int:
    fact: int = 1
    for i in range(1, n + 1):
        fact *= i
        i += 1
    return fact
    print()


print(factorial(5))
print(factorial(3))
