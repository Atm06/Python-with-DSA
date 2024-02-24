"""
Q7. Keep asking numbers from user until the user enters 0. Then display the average of all numbers
"""


def avg():
    total = 0
    count = 0
    while True:
        num = int(input("Enter a number: "))
        if num == 0:
            break
        total += num
        count += 1
        average: float = total / count
    print(f"Average value of the entered numbers is {average}")


avg()
