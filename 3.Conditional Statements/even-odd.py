# Ask a number from user. Print EVEN/ODD

num: int = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")
