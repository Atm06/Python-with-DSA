"""
Make 2 functions.
add() - it will take 3 integers - return the addition

checkOddEven() - it will take 1 integer, check if odd or even
"""


def add(num1: int, num2: int, num3: int):
    total = num1 + num2 + num3
    return total


def checkOddEven(num: int):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")


t = add(3, 4, 5)
print(t)
checkOddEven(33)
