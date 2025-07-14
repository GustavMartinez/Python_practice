
"""
TO DO-1\n- Use a while loop to let the user guess again. \n- The loop should only stop once the user has guessed all the letters in the chosen_word.\n- At that point `display` has no more blanks (\"_\").

TO DO-2\n- Update the for loop so that previous guesses are added to the `display` String.

"""


import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False

correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:

        if letter == guess:
            display = display + letter
            correct_letters.append(letter)

        elif letter in correct_letters:
            display = display + letter

        else:
            display += "_"
    print(display)


    if "_" not in display:
        game_over = True
        print("You win")


