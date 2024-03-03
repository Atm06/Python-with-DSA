"""
Q5. Create a function countOddEven that accepts an List of Integers and
print how many even and odd numbers are there
"""

from typing import List


def countOddEven(lst: List[int]):
    odd_count = 0
    even_count = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print(
        f"There are {odd_count} odd numbers and {even_count} even numbers in the list"
    )


lst = [10, 20, 22, 23, 25, 27, 29, 31, 35, 40, 50, 60, 5, 62]
countOddEven(lst)
