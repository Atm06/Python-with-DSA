"""
Enter a number = 10
Enter a number = 10
Enter a number = 10
Enter a number = 10
Enter a number = 10
Enter a number = 10
Enter a number = 0

when i/p == 0, o/p -> 60
"""

total = 0
while True:
    num: int = int(input("Enter a number: "))
    if num == 0:
        break
    total += num
print(total)
