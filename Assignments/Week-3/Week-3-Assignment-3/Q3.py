"""
Q3. Make a list of your own. Count how many numbers are divisible by 5.
"""

my_list = [10, 20, 33, 35, 34, 36, 40, 45, 49, 50, 55]
count: int = 0
for i in range(len(my_list)):
    if my_list[i] % 5 == 0:
        count += 1
print(f"Total count numbers divisible by 5 in the list is: {count}")
