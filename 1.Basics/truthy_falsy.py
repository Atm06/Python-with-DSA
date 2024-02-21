"""
int -> boolean
float -> boolean
Truthy -> 1 2 3 -5
Falsy -> 0 None [] {} "" 0.0
"""

a = bool(0.0)
print(a)

a = bool(2)
print(a)
"""
str -> bool
Truthy -> "dwadwa" " " "." "dwa wda dawd aw"
Falsy -> ""
"""
a = bool("")
print(a)
