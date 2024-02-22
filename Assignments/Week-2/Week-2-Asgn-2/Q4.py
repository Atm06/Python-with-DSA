"""
Q4. Write a Python program that takes four numbers from the user. 
    Implement a function to find the average of the first three numbers.
    Then, create another function to check if the average is greater than or equal to the fourth number. 
    Make sure to use these two functions to determine 
    and print whether the average is greater than or equal to the fourth number or not
"""


def findaverage(num1: int, num2: int, num3: int) -> float:
    average: float = (num1 + num2 + num3) / 3
    return average


def findgreater(num: float, num4: int) -> bool:
    return num >= num4


num1: int = int(input("Enter first number: "))
num2: int = int(input("Enter second number: "))
num3: int = int(input("Enter third number: "))
num4: int = int(input("Enter fourth number: "))

avg: float = findaverage(num1, num2, num3)
print(f"Average value of the first three numbers is: {avg}")

res: bool = findgreater(avg, num4)

if res:
    print(f"Average value of first three numbers is greater than the fourth number!")
else:
    print(f"Average value of first three numbers is lesser than the fourth number!")
