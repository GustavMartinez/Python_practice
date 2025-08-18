import pandas as pd

PATH_FILE = '/home/gustavo/repos/Python_practice/13_100_days_of_code/Day_21_to_30/Day_25/weather_data.csv'

data = pd.read_csv(PATH_FILE)

print(type(data['temp'])) # this is a serie
print(type(data)) # this is a dataframe


# Convert dataframe to dictionary
data_dict = data.to_dict()
print(data_dict)


# Convert series (column) to list
temp_list = data['temp'].to_list()
print(temp_list)
print(len(temp_list))


# calculate avg of temperatures:
temp_avg = data['temp'].mean()
print(temp_avg)


# max valur of temperaturs:
max_temp = data['temp'].max()
print(max_temp)