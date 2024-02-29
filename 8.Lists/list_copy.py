import copy

a = [56, 32, "Akul", [1, 2, 3], "Ambani", False, 11.112]

"""
#Reference Copy (Saves memory of one list into another)
b = a

print("A ->", a, id(a))
print("B -> ", b, id(b))

b[-1] = 1000

print("A ->", a, id(a))
print("B -> ", b, id(b))

"""
# Shallow copy(Id of a and b will be different)
# Deep copy(Id of a and b will be different)
b = copy.copy(a)  # Shallow Copy
b[-1] = 1000
print("A ->", a, id(a))
print("B -> ", b, id(b))
b = copy.deepcopy(a)  # Deep Copy
print("A ->", a, id(a))
print("B -> ", b, id(b))

b[3][1] = 1000

print("A ->", a, id(a))
print("B -> ", b, id(b))
