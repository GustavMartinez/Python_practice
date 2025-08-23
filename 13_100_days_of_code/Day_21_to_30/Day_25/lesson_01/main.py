
PATH_FILE = '/home/gustavo/Documents/Study/005_Python_General/github/python_practice/13_100_days_of_code/Day_21_to_30/Day_25/weather_data.csv'


w_data = []

with open (PATH_FILE) as file:
    data = file.readlines()
print(data)


