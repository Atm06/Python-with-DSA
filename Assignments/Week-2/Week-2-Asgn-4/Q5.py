"""
Q5. Create a function named pattern which takes an integer as an input and print the following pattern
    pattern(4) -> o/p = 1 2 4 8
    pattern(7) -> o/p = 1 2 4 8 16 32 64
"""


def pattern(num: int):
    i = 0
    res: int = 1
    while i < num:
        res = 2**i
        i += 1
        print(res, end=" ")
    print()


pattern(4)
pattern(7)
