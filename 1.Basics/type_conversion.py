"""
Type Conversion/ Type Casting
To convert from one datatype to another
str -> int
"""

a = "100"  # We'll get value error because of a is not an integer
b = "200"
c = int(a)
d = int(b)

print(a + b)
print(c + d)

# str -> float
a = float("100.5")
b = float("200")
print(a + b)

# float -> int

a = int(
    55.95
)  # 55 will be printed because int will remove the decimal part after rounding it off
print(a)

a = int(-5.56)
print(a)
