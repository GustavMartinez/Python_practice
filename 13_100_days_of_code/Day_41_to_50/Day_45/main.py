from bs4 import BeautifulSoup

PATH_TO_FILE = '/home/gustavo/Documents/Study/005_Python_General/github/python_practice/13_100_days_of_code/Day_41_to_50/Day_45/website.html'

with open(PATH_TO_FILE) as file:
    contents = file.read()


soup = BeautifulSoup(contents, "html.parser")
print(soup.title)
print(soup.title.string)