
"""
TO DO-1 Create an empty String called `placeholder`.\n- For each letter in the chosen_word, add a `_` to `placeholder`.\n- So if the `chosen_word` was \"apple\", `placeholder` should be `_ _ _ _ _` with 5 `\"_\"` representing each letter to guess. Print out `hint`.

TO DO-2 Create an empty string called \"display\".\n- Loop through each letter in the `chosen_word`\n- If the letter at that position matches `guess` then reveal that letter in the `display` at that position.\n- e.g. If the user guessed \"p\" and the chosen word was \"apple\", then `display` should be `_ p p _ _`.\n- Print `display` and you should see the guessed letter in the correct position

"""


import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# Todo 1 - starts here


temp_list = []

for i in chosen_word:
    temp_list.append("_")

placeholder = "".join(temp_list)

print(placeholder)

"""
other solution:

placeholder = ""
word_length = len(chosen_word)

for position in range(word_length):
    placeholder += "_"
print(placeholder)

"""


# Todo 1 - ends here


guess = input("Guess a letter: ").lower()


# Todo 2 - starts here


temp = []

for letter in chosen_word:
    if letter == guess:
        temp.append(letter)
    else:
        temp.append("_")

display = "".join(temp)

print(display)


"""
Other solution:

display = ""

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)

"""

# Todo 2 - ends here