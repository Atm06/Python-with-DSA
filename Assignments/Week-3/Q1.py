"""
Solve pattern using functions

1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""


def pattern():
    for i in range(1, 6):
        for j in range(1, 6):
            print(j, end=" ")
        print()


pattern()
