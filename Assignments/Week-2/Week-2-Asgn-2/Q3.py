"""
Q3. Ask 3 numbers from user. Make a function which returns the middle of those 3 numbers. 
    Then make a function to check if that middle number is divisible by both 3 and 4. 
    Make 2 functions for reusability
"""


def find_middle_number(num1: int, num2: int, num3: int) -> int:
    if (num1 <= num2 <= num3) or (num1 >= num2 >= num3):
        return num2
    elif (num2 <= num1 <= num3) or (num2 >= num1 >= num3):
        return num1
    else:
        return num3


def isdivisibleby3and4(num: int) -> bool:
    return num % 3 == 0 and num % 4 == 0  # This line will directly return True / False


num1: int = int(input("Enter first number: "))
num2: int = int(input("Enter second number: "))
num3: int = int(input("Enter third number: "))

middle_number: int = find_middle_number(num1, num2, num3)
print(f"The middle number is: {middle_number}")

result: bool = isdivisibleby3and4(middle_number)
print(result)
