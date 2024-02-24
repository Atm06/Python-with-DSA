"""
Q1. Create a function named divs, which will take two parameters n1 and n2.
    Return the count of how many numbers from 1 to n1 are divisible by n2
"""


def divs(n1: int, n2: int) -> int:
    count: int = 0
    i = 1
    while i <= n1:
        if i % n2 == 0:
            print(i, end=" ")
            count += 1
        i += 1
    print()
    return count


print(divs(100, 10))
