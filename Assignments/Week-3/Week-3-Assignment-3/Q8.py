"""
Q8. Create a function findSmallest that accepts an List of Integers and
returns the smallest number from the list
"""

from typing import List


def findsmallest(lst: List[int]):
    smallest: int = lst[0]
    for i in range(len(lst)):
        if lst[i] < smallest:
            smallest = lst[i]
    return smallest


lst = [10, 20, 30, 40, 50, 65, 75, 59, 102, 99, 103]
print(f"Largest number in the list of intergers is: {findsmallest(lst)}")
