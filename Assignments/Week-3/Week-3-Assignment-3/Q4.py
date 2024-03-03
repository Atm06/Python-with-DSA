"""
Q4. Make a list of your own. Calculate the length of that list without using
len() function.
"""

my_list = [10, 20, 30, 40, 45, 50, 55, 56, 57, 58, 59, 60]
len: int = 0
for num in my_list:
    len += 1
print(len)
