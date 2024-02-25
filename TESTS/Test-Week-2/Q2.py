"""
Q2. Print all the prime numbers between 1 to 100
"""


def checkfactors(num: int):
    i = 1
    fact_count: int = 0
    while i <= num:
        if num % i == 0:
            fact_count += 1
        i += 1
    return fact_count


def printPrimes():
    for i in range(1, 101):
        if checkfactors(i) == 2:
            print(i, end=" ")
        else:
            pass
        i += 1


printPrimes()
