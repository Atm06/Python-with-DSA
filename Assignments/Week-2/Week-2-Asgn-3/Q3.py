"""
Q3. Create a function named multiplicationTable that takes an integer 
   num as an argument. Print the multiplication table of that number up to 10 numbers.

"""


def multiplicationTable(num: int):
    i = 1
    while i <= 10:
        res: int = num * i
        print(f"{num} * {i} = {res}")
        i += 1
    print()


multiplicationTable(231)
