import random

print("------------------------------------")
print("Welcome to the Number Guessing Game!")
print("------------------------------------")


# Functions

def number_to_guess():
    return random.randint(1,100)

def difficulty():

    level = input("Choose a difficulty. Type 'easy' or 'hard':\n").lower()

    if level == 'easy':
        return 'easy'
    elif level == 'hard':
        return 'hard'
    else:
        print('not a valid input. Try again')
        difficulty()
    
def attemps(user_difficulty, number):
    
    if user_difficulty == 'easy':
        print("You have 5 attempts remaining to guess the number")
        print(f"The number is {number}")
    else:
        print("you have 10 attempts remaining to guess the number")
        print(f"The number is {number}")



# not functions
print("I'm thinking of a number between 1 and 100.")


user_difficulty = difficulty()
number = number_to_guess()
attemps(user_difficulty, number)
