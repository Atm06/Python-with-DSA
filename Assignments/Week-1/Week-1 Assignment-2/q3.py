"""
Q3. Write a program to check if number is divisible by 2 and 3 but not 8.
"""

num: int = int(input("Enter a number"))
"""
if ((num % 2 == 0 and num % 3 == 0) and (num % 8 != 0)):
    print(f"{num} is divisible by both 2 and 3 but not by 8")
else:
    print(f"{num} doesn't meet our specified rules for divisibility)
"""


print(
    f"{num} is divisible by both 2 and 3 but not by 8 "
    if ((num % 2 == 0 and num % 3 == 0) and (num % 8 != 0))
    else "Number doesn't meet our specified rules for divisibility"
)
