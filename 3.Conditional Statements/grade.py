"""
Ask a mark from user, 1-100

91 - 100 -> A
81 - 90 -> B
71 - 80 -> C
61 - 70 -> D
0 - 60 -> FAIL
"""

# Approach -1:
"""
mark: int = int(input("Enter mark secured: "))
if mark > 90 and mark <= 100:
    print("A")
elif mark > 80 and mark <= 90:
    print("B")
elif mark > 70 and mark <= 80:
    print("C")
elif mark > 60 and mark <= 70:
    print("D")
elif mark >= 0 and mark <= 60:
    print("FAIL")
else:
    print("INVALID MARKS")
"""

# Approach -2 :

num: int = int(input("Enter mark = "))

if num >= 91 and num <= 100:
    print("A")
elif num >= 81 and num <= 90:
    print("B")
elif num >= 71 and num <= 80:
    print("C")
elif num >= 61 and num <= 70:
    print("D")
elif num >= 1 and num <= 60:
    print("FAIL")
else:
    print("Invalid Marks")
