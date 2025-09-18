"""

TO DO-1 Randomly choose a word from the word_list and assign it to a variable called `chosen_word`. Then print it.

TO DO-2 Ask the user to guess a letter and assign their answer to a variable called `guess`. Make the String stored in `guess` lowercase.

TO DO-3 Check if the letter the user guessed `guess` is one of the letters in the `chosen_word`. Loop through each of the letters in the `chosen_word`  and print \"Right\" if the letter is a match, \"Wrong\" if it's not.

"""

import random

# list of words to guess
word_list = ["aardvark", "baboon", "camel"]

# create a variable with a random word of the list of words
chosen_word = random.choice(word_list)


print(chosen_word)

# ask the user for a letter and convert it to lower
guess = input("Guess a letter: ").lower()


# evaluate if the letter is in the chosen word
for letter in chosen_word:
    if guess == letter:
        print("Right")
    else:
        print("Wrong")