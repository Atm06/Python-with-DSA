"""
Q3. Write a Python function that takes two lists and returns True if they
have at least one common element
"""

from typing import List


def findCommonElement(lst1: List, lst2: List) -> int:
    count: int = 0
    for i in lst1:
        for j in lst2:
            if i == j:
                count += 1
            else:
                pass
    return count


lst1 = [34, 11, 91, 59, 33, 22]
lst2 = [78, 14, 23, 34]

if findCommonElement(lst1, lst2) >= 1:
    print(True)
else:
    print(False)
