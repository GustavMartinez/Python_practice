"""

TO DO-1 Randomly choose a word from the word_list and assign it to a variable called `chosen_word`. Then print it.

TO DO-2 Ask the user to guess a letter and assign their answer to a variable called `guess`. Make the String stored in `guess` lowercase.

TO DO-3 Check if the letter the user guessed `guess` is one of the letters in the `chosen_word`. Loop through each of the letters in the `chosen_word`  and print \"Right\" if the letter is a match, \"Wrong\" if it's not.

"""
"""
TO DO-1 Create an empty String called `placeholder`.\n- For each letter in the chosen_word, add a `_` to `placeholder`.\n- So if the `chosen_word` was \"apple\", `placeholder` should be `_ _ _ _ _` with 5 `\"_\"` representing each letter to guess. Print out `hint`.

TO DO-2 Create an empty string called \"display\".\n- Loop through each letter in the `chosen_word`\n- If the letter at that position matches `guess` then reveal that letter in the `display` at that position.\n- e.g. If the user guessed \"p\" and the chosen word was \"apple\", then `display` should be `_ p p _ _`.\n- Print `display` and you should see the guessed letter in the correct position

"""
"""
TO DO-1\n- Use a while loop to let the user guess again. \n- The loop should only stop once the user has guessed all the letters in the chosen_word.\n- At that point `display` has no more blanks (\"_\").

TO DO-2\n- Update the for loop so that previous guesses are added to the `display` String.

"""
"""
TO DO-1: \n- Create a variable called `lives` to keep track of the number of lives left.\n- Set `lives` to equal `6`.
TO DO-2: \n- If `guess` is not a letter in the `chosen_word`, Then reduce `lives` by `1`. \n- If `lives` goes down to `0` then the game should end, and it should print \"You lose.
TO DO-3: \n- print the ASCII art from the list `stages` that corresponds to the current number of `lives` the user has remaining.
"""

import random
word_list = ["aardvark", "baboon", "camel"]
lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for letter in chosen_word:
    placeholder+= '_'
print(placeholder)

game_over = False

guess_letters = []
display = ""

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in guess_letters:
        print("You already guess that letter, try a new one")

    display=""

    for letter in chosen_word:
        if letter == guess:
            display+=letter
            guess_letters.append(letter)
        elif letter in guess_letters:
            display+=letter
        else:
            display+= '_'

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong letter, you now have {lives} lives!")


    if not "_" in display:
        print("You win!")
        game_over = True

    if lives == 0:
        print("You lose!, game over")
        game_over = True
        


