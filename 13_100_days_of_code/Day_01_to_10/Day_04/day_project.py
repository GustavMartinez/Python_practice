import random

print("Rock, Paper, Scissor")
print("---------------------")

user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))
computer = random.randint(0,2)

game_options = ["Rock", "Paper", "Scissors"]

user_choose = game_options[user]
computer_choose = game_options[computer]

wins = ""

if user == 0 and computer == 2:
    wins = "You win!"
elif user == 1 and computer == 0:
    wins = "You win!"
elif user == 2 and computer == 1:
    wins = "You win!"
elif user == computer:
    wins = "Draw"
else:
    wins = "computer wins"


print(f"You choose: {user_choose}")
print(f"Computer choose: {computer_choose}")
print(f"Wins: {wins}")