"""
Make a function named checkOddEven
Which takes 1 integer as an argument

If integer is even, then return True
else return False
"""

# def CheckOddEven(num: int) -> bool:
#     if num % 2 == 0:
#         return True
#     else:
#         return False

# print(CheckOddEven(20))

# OPTIMIZED CODE:


# Method - 1:
def CheckOddEven(num: int) -> bool:
    if num % 2 == 0:
        return True
    return False


print(CheckOddEven(20))


# Method - 2:
def CheckOddEven(num: int) -> bool:
    return num % 2 == 0


"""Since the condition only focuses on one condition 
    that is modulus operation w.r.t 2 
    we directly return that condition itself"""
print(CheckOddEven(20))
print(CheckOddEven(11))
