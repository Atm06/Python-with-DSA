start: int = int(input("Enter Start Number: "))
end: int = int(input("Enter End Number: "))
total = 0
for i in range(start, end + 1):
    print(i, end=" ")
    total += i
print()
print(total)
