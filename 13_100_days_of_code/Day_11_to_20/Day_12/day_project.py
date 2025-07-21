print("------------------------------------")
print("Welcome to the Number Guessing Game!")
print("------------------------------------")


# Functions
def difficulty():

    level = input("Choose a difficulty. Type 'easy' or 'hard':\n").lower()

    if level == 'easy':
        return 'easy'
    elif level == 'hard':
        return 'hard'
    else:
        print('not a valid input. Try again')
        difficulty()
    


# not functions
print("I'm thinking of a number between 1 and 100.")


difficulty()