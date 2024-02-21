# Ask a number. YES if number is div by both 5 and 6

num: int = int(input("Enter a number: "))

if num % 5 == 0 and num % 6 == 0:
    print("YES")

else:
    print("NO")
