PATH = "/home/gustavo/repos/Python_practice/13_100_days_of_code/Day_21_to_30/Day_24/lesson_1/my_file.txt"


# mode = "r"  >>> abrir un archivo como solo lectura

with open(PATH, mode="r") as a:
    content = a.read()
    print(content)