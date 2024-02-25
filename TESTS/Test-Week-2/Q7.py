"""
Q7. Create a function named as printPrimeFactors that takes an integer n as a argument 
    and print all the prime factors of that number.
    
    Example if number = 20
    Then the factors of 20 are 1,2,5,10,20.So prime factors are 2,5 (this is the output)
"""


def findfactors(n: int):
    i = 1
    fact_count: int = 0
    while i <= n:
        if n % i == 0:
            fact_count += 1
        i += 1
    if fact_count == 2:
        return True
    else:
        return False


def printPrimeFactors(n: int):
    for i in range(1, n + 1):
        if n % i == 0:
            if findfactors(i):
                print(i, end=" ")
    print()


printPrimeFactors(20)
