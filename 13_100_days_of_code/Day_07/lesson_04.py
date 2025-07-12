
"""
TO DO-1: \n- Create a variable called `lives` to keep track of the number of lives left.\n- Set `lives` to equal `6`.
TO DO-2: \n- If `guess` is not a letter in the `chosen_word`, Then reduce `lives` by `1`. \n- If `lives` goes down to `0` then the game should end, and it should print \"You lose.
TO DO-3: \n- print the ASCII art from the list `stages` that corresponds to the current number of `lives` the user has remaining.
"""

import random

word_list = ["aardvark", "baboon", "camel"]
lives = 6 # To do


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

    if guess not in display: # To do
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose")


    if "_" not in display:
        game_over = True
        print("You win")