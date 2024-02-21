"""
Q1. Write a Python function to find the Maximum and minimum of three numbers. Use 3 parameters.
Make 2 different functions named as maxi and mini
"""


def maxi(a: int, b: int, c: int):
    # without using inbuilt function
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


def mini(a: int, b: int, c: int):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print(f"Maximum number is: {maxi(a, b, c)}")
print(f"Minimum number is: { mini(a, b, c)}")
