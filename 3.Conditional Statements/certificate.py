"""
3 requirements to get a certificate:
    1.Should be part of C&D
    2.Minmum classes attended should be 20
    3. Minimum assignment submitted = 45
User inputs to be taken:

Are you part of C&D = yes/No
    If yes -> Enter class attended
        No -> Can't get cert
Enter assignment submitted = 68
    Eligible for cert
"""

inp1 = input("Are you a part of C & D? \nPlease Enter your Choice : yes/no : ")

if inp1 == "yes":
    classes_attended = int(input("Please enter number of classes attended: "))
    if classes_attended >= 20:
        assignment_submitted = int(
            input("Please enter number of assignments submitted")
        )
        if assignment_submitted >= 45:
            print("Eligible for Certificate")
        else:
            print("Can't get certificate. Assignments submitted less than 45!")
    else:
        print("Number of classes attended is < 20")
else:
    print("Can't get certifiate")
