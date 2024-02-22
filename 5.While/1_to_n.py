def printpattern(n: int) -> None:
    # Print 1 to n using while
    # Ask n from user
    i = 1
    while i <= n:
        print(i, end=" ")
        i += 1
    print()  # New line after printing 1 to n


printpattern(10)
printpattern(5)
