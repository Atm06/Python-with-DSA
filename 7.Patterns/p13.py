"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""

# This pattern for odd number of loop runs ex-> n = 5 or 9 or 11...


def pattern(n):
    for i in range(1, n // 2 + 2):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

    for i in range(n // 2, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


pattern(5)
