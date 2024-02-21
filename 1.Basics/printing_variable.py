name = "Ashutosh"
age = 22
gender = "Male"

# Method 1 (Using Commas)

print("My name is", name)
print("My age is", age)
print("My gender is", gender)

# Method 2(Using +)

print("My name is " + name)
print("My age is " + str(age))
print("My gender is " + gender)

# Method 3(Using %)

print("My name is %s" % name)
print("My age is %d" % age)
print("My gender is %s" % gender)

# Method 4(Using format method)
print("My name is {}".format(name))
print("My age is {}".format(age))
print("My gender is {}".format(gender))

# Method 5 (Using f-string) //Importnant method
print(f"My name is {name}, my age is {age} and my gender is {gender}")

print(f"{name = }")  # name = "Ashutosh" will be printed
