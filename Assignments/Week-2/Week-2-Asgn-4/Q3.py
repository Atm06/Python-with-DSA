"""
Q3. Create a function named factorial which takes a integer as an input and 
    returns the factorial of that number.
"""


def factorial(num: int) -> int:
    if num == 0 or num == 1:
        return 1
    i = 1
    fact = 1
    while i <= num:
        fact *= i
        i += 1
    return fact


print(factorial(5))
