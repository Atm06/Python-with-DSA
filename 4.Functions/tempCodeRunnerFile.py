def CheckOddEven(num: int):
    if(num % 2 == 0):
        return True
    else:
        return False

num: int = int(input("Enter number: "))
CheckOddEven(num)