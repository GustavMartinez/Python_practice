path = '/home/gustavo/Documents/Study/005_Python_General/github/python_practice/13_100_days_of_code/Day_21_to_30/Day_24/lesson_1/my_file.txt'


#with open(path) as file:
#    contents = file.read()
#    print(contents)


with open ('./13_100_days_of_code/Day_21_to_30/Day_24/lesson_2/new_file.txt', mode='a') as file:
    file.write("\nNew text")

