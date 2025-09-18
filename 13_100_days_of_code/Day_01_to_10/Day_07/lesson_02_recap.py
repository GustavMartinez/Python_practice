import random

# list of words to guess
word_list = ["aardvark", "baboon", "camel"]

# create a variable with a random word of the list of words
chosen_word = random.choice(word_list)


placeholder = ""
display = ""


for i in chosen_word:
    placeholder += '_'


print(placeholder)
print(chosen_word)



# ask the user for a letter and convert it to lower
guess = input("Guess a letter: ").lower()


# evaluate if the letter is in the chosen word
for letter in chosen_word:
    if guess == letter:
       display += letter
    else:
        display += '_'


print(display)
