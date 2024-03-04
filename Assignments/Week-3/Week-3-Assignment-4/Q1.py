"""
Q1. Make a list of your own. Make two more empty list like odd and even.
Put all the even numbers from original list to even and odd numbers to
odd and print both lists. (Don’t remove anything from original one)
"""

lst1 = [11, 12, 24, 26, 28, 34, 35, 39, 42, 45, 49, 50, 52, 56, 60]
even_list = []
odd_list = []

for i in range(len(lst1)):
    if lst1[i] % 2 == 0:
        even_list.append(lst1[i])
    else:
        odd_list.append(lst1[i])
print(even_list)
print(odd_list)
