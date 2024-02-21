"""
Logical Operators (To compare two values or expressions)

AND

C1  C2  Result
F   F   F
F   T   F
T   F   F
T   T   T

OR

C1  C2  Result
F   F   F
F   T   T
T   F   T
T   T   T

NOT

C1  Result
F   T
T   F

XOR - Exclusive OR

"""

physics = 16
chemistry = 20

# print(physics > 33 and chemistry > 33)

# print(physics > 33 or chemistry > 33)

print(not (physics > 33 or not chemistry > 33))
