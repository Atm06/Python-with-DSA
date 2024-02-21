"""
WEEK 1 - ASSIGNMENT-1 : BASICS

Q1. There are two variables.a=5 b=10What will be the output of following:
Q2. Python program to convert kilometers to miles. Ask kilometer from User.
Q3. Ask 3 numbers from User and Calculate the Average.
Q4. Ask value in Rupees and Convert into Paise.
Q5. Calculate Area of Square by taking side from User.
Q6. Ask number of games played in a tournament. Ask the user number of games won and number of games loss. Calculate number of tie and total Points. (1 win= 4 points, 1 tie =2 points)

"""

# ==========================================================================
# Q1. Solution:

# a = 5
# b = 10

# print(a > 5 and b >= 10)  # False
# print(a >= 5 or not b > 10)  # True
# print(not (a > 5 and b > 5))  # True
# print(not (a < 10 or not b < 10))  # False
# print(not (not a <= 5 or not b >= 10))  # True

# ===========================================================================

# Q2. Solution: Python program to convert kilometers to miles. Ask kilometer from User.


# kilometer_value = int(input("Please Enter the kilometer value: "))
# miles_value = kilometer_value * 0.621371
# print(f"Miles value of {kilometer_value} kilometers is: {miles_value}")

# ===========================================================================

# Q3. Solution: Ask 3 numbers from User and Calculate the Average.

# num1 = int(input("Please Enter the 1st number: "))
# num2 = int(input("Please Enter the 2nd number: "))
# num3 = int(input("Please Enter the 3rd number: "))

# avg_value = (num1 + num2 + num3) / 3
# print(f"Average of {num1}, {num2} and {num3} is: {avg_value}")

# print(f"Average = {avg_value:.2f}")  # To display output upto 2 decimals only

# =============================================================================

# Q4. Solution: Ask value in Rupees and Convert into Paise.

# rupees_value = int(input("Please Enter the amount in Rupees: "))
# paise_value = rupees_value * 100
# print(f"Amount in Paise is: {paise_value}")

# =============================================================================

# Q5. Solution: Calculate Area of Square by taking side from User.

# side_length = float(input("Enter Side Length of Square: "))
# area = side_length**2
# print(f"Area of Square is: {area} square units")

# print(f"Area of square with {side_length} side = {area:.2f}")

# =============================================================================

# Q6. Solution: Ask number of games played in a tournament. Ask the user number of games won and number of games loss. Calculate number of tie and total Points. (1 win= 4 points, 1 tie =2 points)

# games_played = int(input("Enter the total number of games played:"))
# games_won = int(input("Enter the number of games won:"))
# games_lost = int(input("Enter the number of games lost:"))

# tied_games = games_played - (games_won + games_lost)

# total_points_earned = games_won * 4 + tied_games * 2

# print(f"Total Points secured is {total_points_earned}")

# =============================================================================

"""
IF-ELSE QUESTIONS:
Q7. Check if the number entered by User is divisible by 3 or not.
Q8. Ask a number from user. Print if the number is ODD or EVEN.
Q9. Take values of length and breadth of a rectangle from user and check if
it is square or not
"""

# =============================================================================

# Q7. Solution: Check if the number entered by User is divisible by 3 or not.

# num = int(input("Enter a number: "))
# if num % 3 == 0:
#     print(f"{num} is divisible by 3")
# else:
#     print(f"{num} is not divisible by 3")

# =============================================================================

# Q8. Solution: Ask a number from user. Print if the number is ODD or EVEN.

# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(f"{num} is an even number")
# else:
#     print(f"{num} is an odd number")

# =============================================================================

# Q9. Solution: Take values of length and breadth of a rectangle from user and check if it is square or not.

# length = int(input("Enter length of rectangle: "))
# breadth = int(input("Enter breadth of rectangle: "))

# if length == breadth:
#     print("Given rectangle is a square")
# else:
#     print("Given rectangle is not a square")
