"""
Ask a number from user.

If div. by 3 -> FOO
If div by 5 -> BAR
If div by both 3 and 5 -> FOOBAR
else - > FOOFOOBARBAR
"""

num: int = int(input("Enter a number: "))

if num % 3 == 0 and num % 5 == 0:
    print("FOOBAR")
elif num % 3 == 0:
    print("FOO")
elif num % 5 == 0:
    print("BAR")
else:
    print("FOOFOOBARBAR")
