"""
Q9. Create a function updateOddEven that accepts an List of Integers and
update all the even numbers to 0 and update all the odd numbers to 1
"""

from typing import List


def updateOddEven(lst: List[int]):
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst[i] = 0
        else:
            lst[i] = 1
    return lst


lst = [10, 20, 22, 23, 25, 27, 29, 31, 35, 40, 50, 60, 5, 62]
print(updateOddEven(lst))
