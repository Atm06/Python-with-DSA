"""
Q4. Attempt Week 1 - Assignment 2 (Q6) using function.
     Ask 4 numbers from user. 
     Make sure all the numbers entered by user are dierent. 
     Print which number is the smallest.
    
   -> Attempt Week 1 - Assignment 2 (Q7) using function.
    
    Take Salary as input from User and Update the salary of an employee
    salary less than 10,000, 5 % increment
    salary between 10,000 and 20, 000, 10 % increment
    salary between 20,000 and 50,000, 15 % increment
    salary more than 50,000, 20 % increment

"""


# Week-1-asgn-2-Q6.
def smallest_number(num1, num2, num3, num4):
    smallest = num1
    if num2 < smallest:
        smallest = num2
    if num3 < smallest:
        smallest = num3
    if num4 < smallest:
        smallest = num4
    return smallest


num1: int = int(input("Enter first number: "))
num2: int = int(input("Enter second number: "))
num3: int = int(input("Enter third number: "))
num4: int = int(input("Enter fourth number: "))

print(f"Smallest number is: {smallest_number(num1, num2, num3, num4)}")


# Week-1-asgn-2-Q7


def salary_update(salary: int):
    if salary < 10000:
        increment = salary * 0.05
    elif 10000 <= salary <= 20000:
        increment = salary * 0.1
    elif 20000 <= salary <= 50000:
        increment = salary * 0.15
    elif salary > 50000:
        increment = salary * 0.2
    else:
        print("Invalid Value")
    updated_salary = salary + increment

    return updated_salary


salary: int = int(input("Enter your current salary: "))
print(f"Your updated salary after increment is : {salary_update(salary)}")
