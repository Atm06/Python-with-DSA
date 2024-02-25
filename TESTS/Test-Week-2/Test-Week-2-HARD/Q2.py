"""
Q2. Make a function named checkPalindrome which accepts an integer n from the user. 
    Return True or False if the number is palindrome or not. 
    Palindrome means which is same as forward and backwards. Do not use STRINGS
"""


def reverseNum(n: int):
    rev: int = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev


def checkPalindrome(n: int) -> bool:
    while n > 0:
        if n == reverseNum(n):
            return True
        else:
            return False
    print()


print(checkPalindrome(111))
print(checkPalindrome(91))
print(checkPalindrome(1221))
print(checkPalindrome(9854))
print(checkPalindrome(123454321))
