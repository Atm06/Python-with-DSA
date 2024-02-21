"""
Q2.Attempt the same leap year question (Week 1 - Assignment 2 - Q8) but using function. 
Try calling function with different years as a parameter and check the result.
"""


def find_leap_year(year: int):
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print("A Leap year")
    else:
        print("Not a leap year")


year: int = int(input("Enter the year: "))
find_leap_year(year)
