"""
Q6. Don’t create a function, just print the following pattern 1  11  111  1111  11111....n times (Ask n from user)
"""

num: int = int(input("Enter a number: "))
i = 1
res = 1
while i < num:
    print(res, end=" ")
    res = (res * 10) + 1
    i += 1
