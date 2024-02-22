"""
Q2. Implement a function that takes two parameters, base and exponent,
     and returns the result of raising the base to the power of the exponent.
"""


def power_exponent(base: int, exponenet: int):
    res: int = base**exponenet
    return res


print(power_exponent(2, 3))
