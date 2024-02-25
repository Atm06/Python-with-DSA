"""
Q4. Make a function named checkArmstrong which accepts an integer n 
    from the user. Return True or False if that number is an armstrong number
"""


def checkArmstrong(num: int) -> bool:
    sum: int = 0
    n = num  # storing n in a variable "num" as "n" value will be changed
    while n > 0:
        digit = n % 10
        sum += digit**3
        n //= 10
    if sum == num:
        return True
    else:
        return False
    print()


print(checkArmstrong(153))
print(checkArmstrong(407))
