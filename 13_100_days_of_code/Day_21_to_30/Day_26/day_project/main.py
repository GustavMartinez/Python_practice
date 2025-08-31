"""
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# Todo 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

# Todo 2. Create a list of the phonetic code words from a word that the user inputs.

"""

import pandas as pd

PATH_FILE = '/home/gustavo/Documents/Study/005_Python_General/github/python_practice/13_100_days_of_code/Day_21_to_30/Day_26/day_project/nato_phonetic_alphabet.csv'

file = pd.read_csv(PATH_FILE)

data = {row.letter:row.code for (index, row) in file.iterrows()}
print(data)


