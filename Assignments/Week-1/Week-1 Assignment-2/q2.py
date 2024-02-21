"""
Q2. A student will not be allowed to sit in exam if his/her attendance is less
than 75%.
Take following input from user

Number of classes held
Number of classes attended.
1. Print percentage of class attended
2. Print Is student is allowed to sit in exam or not
"""

num_of_classes_held: int = int(input("Enter number of classes held: "))
num_of_classes_attended: int = int(input("Enter number of classes attended: "))

if num_of_classes_attended == num_of_classes_held:
    print("Student is allowed to sit in exam")
elif num_of_classes_attended > num_of_classes_held:
    print("Please provide a valid input! You can't be serious!!")
else:
    percentage_of_class_attended: float = (
        num_of_classes_attended / num_of_classes_held
    ) * 100
    print(f"percentage of classes attended is : {percentage_of_class_attended:.2f}%")
    if percentage_of_class_attended >= 75:
        print("Allowed to sit in exam")
    else:
        print("Be prepared for Supplimentary exam!!")
