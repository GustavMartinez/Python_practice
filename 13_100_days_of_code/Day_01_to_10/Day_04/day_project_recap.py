# goal: rock, paper, scissor game!

import random as rd

options = ['Rock', 'Paper', 'Scissors']

# Game of the user:
user_input = int(input("Choose: 0 for Rock; 1 for Paper; or 2 for Scissors \n"))


user_choose = options[user_input]
pc_choose = options[rd.randint(0,2)]


print(f"You choose: {user_choose}")
print(f"PC choose: {pc_choose}")

if user_choose == options[0] and pc_choose == options[2]:
    print('User wins!')

elif user_choose == options[1] and pc_choose == options[0]:
    print('User wins!')

elif user_choose == options[2] and pc_choose == options[1]:
    print('User wins"')

elif user_choose == pc_choose:
    print("Draw")

else:
    print('Computer Wins!')
