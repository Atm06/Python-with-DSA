"""
Q9. Ask a number from user. Print if that number is prime or not, use functions.
"""


def isprime(num: int):
    i = 2
    count = 0
    while i < num:
        if num % i == 0:
            count += 1
        i += 1
    if count >= 1:
        print("Not a Prime Number")
    else:
        print("Prime Number")


num: int = int(input("Enter a number: "))
isprime(num)
