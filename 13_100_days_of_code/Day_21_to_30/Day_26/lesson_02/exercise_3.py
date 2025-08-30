"""
Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line. 

You are going to create a list called result which contains the numbers that are common in both files. 

e.g. if file1.txt contained: 

1 

2 

3

and file2.txt contained: 

2

3

4

result = [2, 3]



IMPORTANT:  The output should be a list of integers and not strings!

Try to use List Comprehension instead of a Loop. 
"""

PATH_FILE_1 = '/home/gustavo/repos/Python_practice/13_100_days_of_code/Day_21_to_30/Day_26/lesson_02/file1.txt'
PATH_FILE_2 = '/home/gustavo/repos/Python_practice/13_100_days_of_code/Day_21_to_30/Day_26/lesson_02/file2.txt'

file_1 = []
file_2 = []

with open(PATH_FILE_1) as file:
    numbers = file.readlines()
    for n in numbers:
        n = int(n.rstrip())
        file_1.append(n)


with open(PATH_FILE_2) as file2:
    other_numbers = file2.readlines()
    for i in other_numbers:
        i = int(i.rstrip())
        file_2.append(i)

# result = [new for item in list if condition]

result = [i for i in file_1 if i in file_2 ]
print(result)