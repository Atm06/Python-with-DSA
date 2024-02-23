"""
            ** Important observation **

Ask a number from user = 50
print -50 to 50

Ask a number from user = 10
print -10 to 10

Ask a number from user = -13
print 13 to -13

Ask a number from user = 20
print 20 to -20
"""


def negative(num: int):
    if num > 0:
        start = -1 * num  # -50
        end = num  # 50
        i = start  # -50
        while i <= end:  # -50 <= 50
            print(i, end=" ")
            i += 1
    else:
        start = -1 * num  # 13
        end = num  # -13
        i = start  # 13
        while i >= end:  # 13 >= -13
            print(i, end=" ")
            i -= 1


num: int = int(input("Enter a number: "))
negative(num)
