"""
Q5. Create a function named printPattern that takes one integer (num) as an argument. 
    Print from -num to num. Also keep in mind number passed as an argument can be negative or positive.
"""


def printPattern(num: int):
    i: int = 0
    if num < 0:
        i = num
        while i <= -num:
            print(i, end=" ")
            i += 1
    else:
        i = -num
        while i <= num:
            print(i, end=" ")
            i += 1


printPattern(-9)
