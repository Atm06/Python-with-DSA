"""
Q4. Create a function named pattern which takes an integer as an input and print the following pattern
    pattern(4) -> o/p = 10 20 30 40
"""


def pattern(num: int):
    i = 1
    while i <= num:
        print(i * 10, end=" ")
        i += 1
    print()


pattern(4)
pattern(11)
