
NAMES_PATH = '/home/gustavo/Documents/Study/005_Python_General/github/python_practice/13_100_days_of_code/Day_21_to_30/Day_24/day_project/input/names/invited_names.txt'
LETTER_TEMPLATE_PATH = '/home/gustavo/Documents/Study/005_Python_General/github/python_practice/13_100_days_of_code/Day_21_to_30/Day_24/day_project/input/letters/starting_letter.txt'
TO_SEND = '/home/gustavo/Documents/Study/005_Python_General/github/python_practice/13_100_days_of_code/Day_21_to_30/Day_24/day_project/output/ready_to_send'


name_list = []

names = open(NAMES_PATH, 'r')

for name in names:
    name = name.rstrip() # removes the space at the end
    name_list.append(name)


for name in name_list:
    with open(LETTER_TEMPLATE_PATH) as content:
        letter = content.read()
        final_doc = letter.replace('[name]', name)
        
        with open (f'{TO_SEND}/letter_for_{name}.txt', mode='a') as file:
            file.write(final_doc)


