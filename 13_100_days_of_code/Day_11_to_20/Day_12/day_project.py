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


def game(number, attemps):
    
    user_attemps = attemps


    print(f"You have {user_attemps} attempts remaining to guess the number")

    user_number = int(input("Make a guess: "))

    while user_number != number and user_attemps > 1:
        user_attemps -= 1

        if user_number > number:
            print("Too high")
        else:
            print("Too low")
        print("Guess again.")
        print(f"You have {user_attemps} attempts remaining to guess the number")
        user_number = int(input("Make a guess: "))
    
    if user_attemps == 1:
        print("You've run out of guesses. Refresh the page to run again")

    if user_number == number:
        print(f"You got it!, the answer is {number}")

def attemps(user_difficulty):
    
    if user_difficulty == 'easy':
        return 10
    else:
        return 5




# not functions
print("I'm thinking of a number between 1 and 100.")


user_difficulty = difficulty()
number = number_to_guess()
attemps = attemps(user_difficulty)

game(number, attemps)