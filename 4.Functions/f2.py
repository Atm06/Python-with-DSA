"""
Make 4 functions - add, sub, mul, div

Ask two numbers 
"""


def add():
    a: int = int(input("Enter first number"))
    b: int = int(input("Enter second number"))
    print(a + b)


def sub():
    a: int = int(input("Enter first number"))
    b: int = int(input("Enter second number"))

    print(a - b)


def mul():
    a: int = int(input("Enter first number"))
    b: int = int(input("Enter second number"))

    print(a * b)


def div(a, b):
    a: int = int(input("Enter first number"))
    b: int = int(input("Enter second number"))

    print(a / b)


add()
sub()
mul()
div()
