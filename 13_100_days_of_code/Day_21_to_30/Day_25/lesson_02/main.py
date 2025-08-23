import csv

PATH_FILE = '/home/gustavo/Documents/Study/005_Python_General/github/python_practice/13_100_days_of_code/Day_21_to_30/Day_25/weather_data.csv'


# Extract data from column 'temp'
with open(PATH_FILE) as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

    print(temperatures)