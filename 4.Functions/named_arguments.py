def totalMarks(
    physics: int, chemistry: int, maths: int, english: int = 0, computer: int = 0
):
    print(f"{physics = }")
    print(f"{chemistry = }")
    print(f"{maths = }")
    print(f"{english = }")
    print(f"{computer = }")
    total = physics + chemistry + maths + english + computer
    print(f"Total marks = {total}")


# totalMarks(english=54, physics=23, chemistry=78, computer=100, maths=78)
# totalMarks(59, 100, english=34, computer=11, maths=98)
totalMarks(45, 55, 85, computer=100)


def personal_details(fname: str, lname: str, age: int = 0, gender: str = "Male"):
    print(f"{fname =}")
    print(f"{lname = }")
    print(f"{age = }")
    print(f"{gender = }")


personal_details("Ashutosh", "Mallick", age=22)
