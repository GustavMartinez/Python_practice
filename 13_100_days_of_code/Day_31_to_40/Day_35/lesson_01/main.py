import requests
import json
import api_key

# Save the response in:

PATH_TO_SAVE = '/home/gustavo/Documents/Study/005_Python_General/github/python_practice/13_100_days_of_code/Day_31_to_40/Day_35/lesson_01/'

# To use the API I need to create an API key
API_KEY = api_key.API_KEY

# The API works with the latitude and longitude, so I need those values
LATITUDE = -19.918180
LONGITUDE = -43.937050

parameters = {
    'lat': LATITUDE,
    'lon': LONGITUDE,
    'appid': API_KEY,
    'cnt': 4            # new parameter to return just 4 timestamps
}

#response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast?lat=-19.918180&lon=-43.937050&appid=937d94de74dac20e86fdce71e0eda333')

# Make the request
response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast', params=parameters)

# Raise the status
response.raise_for_status()

# get the status
status = response.status_code

# save the json response to a variable
data = response.json()

# print the status
print(status)

# Save the response to a json file:
with open(f"{PATH_TO_SAVE}weather_data_4_days.json", 'w') as file:
    json.dump(data, file, indent=4)