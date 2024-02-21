# With Paramters, without Return


def greet(name: str, age: int, gender: str):
    name = ""
    age = 0
    gender = ""
    print(f"My Name is = {name}")
    print(f"My age is = {age}")
    print(f"My gender is = {gender}")


name = "Ashutosh"
age = 22
gender = "Male"
greet(name, age, gender)
print(name, age, gender)
