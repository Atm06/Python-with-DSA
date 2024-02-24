"""
Q2. From 1 to 2000, print all the LEAP YEARS, using WHILE loop.
"""

# Method - 1


# def leap_year():
#     i = 1
#     while i <= 2000:
#         if ((i % 4 == 0) and (i % 100 != 0)) or (i % 400 == 0):
#             print(i, end=" ")
#         i += 1


# leap_year()


# Method -2
def isLeapYear(year: int) -> bool:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


i = 1
while i <= 2000:
    if isLeapYear(i):
        print(i, end=" ")
    i += 1
