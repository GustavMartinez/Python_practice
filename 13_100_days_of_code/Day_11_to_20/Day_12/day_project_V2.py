import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0

def  check_answer(user_guess, actual_answer, turns):
    """Chechs answer against guess, returns the number of turns remaining"""
    if user_guess > actual_answer:
        print("Too high")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it. The answer was {actual_answer}")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard':\n").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS



def game():
    print("------------------------------------")
    print("Welcome to the Number Guessing Game!")
    print("------------------------------------")

    print("I'm thinking of a number between 1 and 100.")

    answer = random.randint(1, 100)
    print(f"{answer}")

    turns = set_difficulty()
    

    guess = 0

    while guess != answer:

        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("Out of guesses")
            return
        elif guess != answer:
            print("Guess again")


game()