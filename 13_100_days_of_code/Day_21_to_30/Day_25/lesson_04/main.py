import pandas as pd

DATA_PATH = '/home/gustavo/repos/Python_practice/13_100_days_of_code/Day_21_to_30/Day_25/lesson_04/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv'
DATA_TO = '/home/gustavo/repos/Python_practice/13_100_days_of_code/Day_21_to_30/Day_25/'

data = pd.read_csv(DATA_PATH)

fur_color = data['Primary Fur Color'].value_counts().rename_axis("Fur Color")

fur_color.to_csv(f'{DATA_TO}fur_color.csv')

