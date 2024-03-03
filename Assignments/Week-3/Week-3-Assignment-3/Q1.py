"""
Q1. Make a list of your own. Print the whole list in reverse using FOR loop
and WHILE loop
"""

lst1 = [10, 20, 30, 40, 50, 60]

# Using For loop
for i in range(-1, -(len(lst1) + 1), -1):
    print(lst1[i], end=" ")
print()
# Using while loop
my_list = [43, 65, "Elon", "Ambani", False, 55.43]

i = 0
while i < len(my_list):
    print(my_list[i], end=" ")
    i += 1
