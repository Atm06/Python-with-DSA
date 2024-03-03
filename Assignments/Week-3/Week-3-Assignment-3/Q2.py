"""
Q2. Make a list of your own. Print all the numbers divisible by 3 and 4 in
that list
"""

my_list = [12, 13, 24, 34, 40, 24, 36]
res = []
for i in range(len(my_list)):
    if my_list[i] % 3 == 0 and my_list[i] % 4 == 0:
        res.append(my_list[i])
print(f"Numbers divisible by 3 and 4 in the list are: {res}", end=" ")
