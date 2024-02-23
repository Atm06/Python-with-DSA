"""
Finding sum of all the digits of a number
"""

num: int = int(input("Enter a number: "))  # 123
total = 0
while num > 0:
    last_diigit = num % 10
    total += last_diigit
    num = num // 10
print(f"Sum of all the digits of a number is: {total}")
