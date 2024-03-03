"""
Q6. Create a function sumCountOddEven that accepts an List of Integers
and calculate sum of even and odd numbers
"""

from typing import List


def sumCountOddEven(lst: List[int]):
    odd_sum = 0
    even_sum = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even_sum += lst[i]
        else:
            odd_sum += lst[i]
    print(
        f"Sum of odd numbers is {odd_sum} and Sum of even numbers is {even_sum} respectively"
    )


lst = [10, 20, 22, 23, 25, 27, 29, 31, 35, 40, 50, 60, 5, 62]
sumCountOddEven(lst)
