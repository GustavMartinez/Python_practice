import random

# list of words to guess
word_list = ["aardvark", "baboon", "camel"]

# create a variable with a random word of the list of words
chosen_word = random.choice(word_list)


"""
TO DO-1\n- Use a while loop to let the user guess again. \n- The loop should only stop once the user has guessed all the letters in the chosen_word.\n- At that point `display` has no more blanks (\"_\").

TO DO-2\n- Update the for loop so that previous guesses are added to the `display` String.

"""


placeholder = ""



for i in chosen_word:
    placeholder += '_'


print(placeholder)
print(chosen_word)


game_over = False
correct_letters = []


while not game_over:

# ask the user for a letter and convert it to lower
    guess = input("Guess a letter: ").lower()

    display = ""

    # evaluate if the letter is in the chosen word
    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(letter)
        
        elif letter in correct_letters:
            display += letter
        else:
            display += '_'


    print(display)

    if "_" not in display:
        
        game_over = True
        print("You win")