"""
Q4. Write a Python Program to find sum and average of List in Python
"""

from typing import List


def findSumandAvg(lst1: List):
    sum: int = 0
    avg: float = 0.0
    for i in lst1:
        sum += i
    avg = sum / len(lst1)
    print(f"Sum of elements in list is {sum} and average value of elements is {avg}")


lst1 = [11, 12, 13, 14, 15]
findSumandAvg(lst1)
