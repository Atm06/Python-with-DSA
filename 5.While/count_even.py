# 1 to 100,,, how many even numbers are there?


def findeven(start: int, end: int) -> int:
    even = 0
    i = start
    while i <= end:
        if i % 2 == 0:
            even += 1
        i += 1
    return even


start: int = int(input("Enter the start number: "))
end: int = int(input("Enter the end number: "))
print(f"Total even numbers between {start} and {end} is = {findeven(start, end)}")
