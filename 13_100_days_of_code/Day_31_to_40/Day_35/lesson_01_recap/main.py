import requests
import json
import api_key

PATH_TO_SAVE = '/home/gustavo/Documents/Study/005_Python_General/github/python_practice/13_100_days_of_code/Day_31_to_40/Day_35/lesson_01_recap/'

API_KEY = api_key.API_KEY

LATITUDE = -19.918180
LONGITUDE = -43.937050

parameters = {
    'lat': LATITUDE,
    'lon': LONGITUDE,
    'appid': API_KEY,
    'cnt': 4
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast', params=parameters)
response.raise_for_status()

status = response.status_code

print(status)

data = response.json()

with open(f'{PATH_TO_SAVE}four_days_forecast.json', 'w') as file:
    json.dump(data, file, indent=4)