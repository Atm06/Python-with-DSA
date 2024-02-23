def sum_div(n1: int, n2: int) -> int:
    # n1 = 64
    # n2 = 3
    total = 0
    i = 1
    while i <= n1:
        if i % n2 == 0:
            total += i
        i += 1
    return total


print(sum_div(100, 8))
