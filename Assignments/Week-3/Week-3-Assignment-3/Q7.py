"""
Q7. Create a function findLargest that accepts an List of Integers and
returns the largest number from the list
"""

from typing import List


def findLargest(lst: List[int]):
    largest: int = lst[0]
    for i in range(len(lst)):
        if lst[i] > largest:
            largest = lst[i]
    return largest


lst = [10, 20, 30, 40, 50, 65, 75, 59, 102, 99, 103]
print(f"Largest number in the list of intergers is: {findLargest(lst)}")
