"""
Q6. Write a program to remove the nth index element from a list using a
function
"""

from typing import List


def removenthElement(lst: List):
    for i in range(len(lst)):
        if i == n:
            lst.remove(lst[i])
    return lst


lst = [10, 11, 12, 13, 14, 15, 16]
n: int = 3

print(removenthElement(lst))

# Alternate Way

"""
Write a program to remove the nth index element from a list using a function.
"""
"""
from typing import List


def removeNth(lst: List, n: int) -> None:
    lst.pop(n)


my_list = [9008, 9102, 4311, 222, 98]
removeNth(my_list, 2)
print(my_list)

"""
