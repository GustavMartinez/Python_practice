
PATH_LETTER = '/home/gustavo/Documents/Study/005_Python_General/github/python_practice/13_100_days_of_code/Day_21_to_30/Day_24/day_project_recap/input/letters/starting_letters.txt'
PATH_NAMES = '/home/gustavo/Documents/Study/005_Python_General/github/python_practice/13_100_days_of_code/Day_21_to_30/Day_24/day_project_recap/input/names/invited_names.txt'
PATH_OUTPUT = '/home/gustavo/Documents/Study/005_Python_General/github/python_practice/13_100_days_of_code/Day_21_to_30/Day_24/day_project_recap/output/ready_to_send'


# Extract names and stored in a new list:

list_of_names = []

with open(PATH_NAMES, mode='r') as file_names:
    names = file_names.readlines()
    for name in names:
        name = name.rstrip()
        list_of_names.append(name)


# Extract letter and update the names:

with open(PATH_LETTER) as file_letter:
    letter = file_letter.read()
    for i in list_of_names:
        new_letter = letter.replace('[name]', i)
        with open (f'{PATH_OUTPUT}/letter_for_{i}', mode='w') as final_letter:
            final_letter.write(new_letter)
