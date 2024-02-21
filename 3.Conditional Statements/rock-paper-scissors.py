"""
Rock Paper Scissors

computer_choice = rock/paper/scissor (selected randomly)

user_choice = input() -> rock/paper/scissor

if
elif
elif

You Won
You Lost, the computer chose rock/paper/scissor
Match Tied
"""

# Approach -1:
"""
import random

options = []
options.append("rock")
options.append("paper")
options.append("scissor")

computer_choice = random.choice(options)
print(f"Computer's choice is: {computer_choice}")

user_choice: str = input("Enter your choice: ")

if user_choice != "rock" and user_choice != "paper" and user_choice != "scissor":
    print("Invalid Choice")
elif user_choice == computer_choice:
    print("Match Tied")
elif (
    (user_choice == "rock" and computer_choice == "scissor")
    or (user_choice == "paper" and computer_choice == "rock")
    or (user_choice == "scissor" and computer_choice == "paper")
):
    print("You Won")
else:
    print(f"You Lost, the computer chose {computer_choice}")

"""
# Approach 2:

import random

options = ["rock", "paper", "scissors"]

computer_choice = random.choice(options)
user_choice = input("Enter rock/paper/scissors = ")

# IF-ELIF-ELIF

if user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
    print("INVALID")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You won")
elif user_choice == "paper" and computer_choice == "rock":
    print("You won")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You won")
elif user_choice == computer_choice:
    print("You tied")
else:
    print(f"You lost, computer choose {computer_choice}")
