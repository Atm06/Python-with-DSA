# 1 to 10 ,,, total
# start, end | start < end
# start, end --- find total

"""
Enter start = 1
Enter end = 10

o/p : Addition of all numbers from 1 to 10 = 55
"""


def total(start: int, end: int) -> int:
    total = 0
    i = start
    while i <= end:
        total += i
        i += 1
    return total


start: int = int(input("Enter start value: "))
end: int = int(input("Enter end value: "))
print(f"Addition of all numbers from 1 to 10 = {total(start, end)}")
