
PATH_FILE_1 = '/home/gustavo/Documents/Study/005_Python_General/github/python_practice/13_100_days_of_code/Day_21_to_30/Day_26/lesson_02/file1.txt'
PATH_FILE_2 = '/home/gustavo/Documents/Study/005_Python_General/github/python_practice/13_100_days_of_code/Day_21_to_30/Day_26/lesson_02/file2.txt'


file_1 = []
file_2 = []

with open(PATH_FILE_1) as file1:
    content1 = file1.readlines()
    file_1 = [int(number.rstrip()) for number in content1]

with open(PATH_FILE_2) as file2:
    content2 = file2.readlines()
    file_2 = [int(number.rstrip()) for number in content2]
    

result = [i for i in file_1 if i in file_2]


print(result)