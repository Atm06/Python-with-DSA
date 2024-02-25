"""
Q1. Create a function named as checkPrime that takes an integer as an argument.
    Print YES if the number passed is a prime number else print NO
"""


def checkPrime(num: int):
    fact_count: int = 0
    for i in range(1, num + 1):
        if num % i == 0:
            fact_count += 1
    if fact_count == 2:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
    print()


checkPrime(9)
checkPrime(3)
