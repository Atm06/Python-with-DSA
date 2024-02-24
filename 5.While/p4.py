# 1 11 101 1001 10001 100001
# Print the pattern


def pattern(n: int):
    i = 1
    number = 1
    while i <= n:
        print(number, end=" ")
        number = (
            10**i
        ) + 1  # First value of number "1" will be printed then value of number will change
        i += 1
    print()


pattern(5)
pattern(10)
