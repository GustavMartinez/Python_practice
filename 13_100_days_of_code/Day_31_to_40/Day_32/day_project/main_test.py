##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas as pd
import datetime as dt

DATA_PATH = '/home/gustavo/Documents/Study/005_Python_General/github/python_practice/13_100_days_of_code/Day_31_to_40/Day_32/day_project/birthdays.csv'




# Read database
data = pd.read_csv(DATA_PATH)

# Create an object to know the month and day
now = dt.datetime.now()
month = now.month
day = now.day

dicts = data.to_dict(orient='records') # or records


for i in dicts:
    if month in i['month']:
        print(i.get('name'))








# if month in dicts['month'] and day in dicts['day']:
#     x = dicts['month'].index(month)
#     nam = dicts['name'][x]
#     print(nam)

