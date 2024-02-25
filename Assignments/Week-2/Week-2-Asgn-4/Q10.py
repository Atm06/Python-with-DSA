"""
Q10. Ask a number from user n1. From 1 to n1, print how many prime numbers are there.
"""

# Method -1


def countprime(n1: int):
    i = 1
    factor_count: int = 0
    while i <= n1:
        if n1 % i == 0:
            factor_count += 1
        i += 1

    if factor_count == 2:
        return True
    else:
        return False


i = 1
n1: int = int(input("Enter a number: "))
prime_count: int = 0
while i <= n1:
    if countprime(i):
        prime_count += 1
    i += 1

print(f"Total prime numbers between 1 to {n1} = {prime_count}")


# Alternate way
def factorsCount(n: int) -> int:
    i = 1
    count = 0
    while i <= n:
        if n % i == 0:
            count += 1
        i += 1
    return count


def isPrime(n: int) -> bool:
    fc = factorsCount(n)
    if fc == 2:
        return True
    else:
        return False


i = 1
n1 = int(input("Enter a number = "))  # 15
count = 0
while i <= n1:
    if isPrime(i):
        count += 1
    i += 1

print(f"Total prime numbers between 1 to {n1} = {count}")
