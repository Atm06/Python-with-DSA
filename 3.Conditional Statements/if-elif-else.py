"""
Ask a number from user. Print positive, negative or equal to zero

"""

num: int = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Equal to zero")
