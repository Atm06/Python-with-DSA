"""
Q10. Ask a number from user n1. From 1 to n1, print how many prime numbers are there.
"""


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
