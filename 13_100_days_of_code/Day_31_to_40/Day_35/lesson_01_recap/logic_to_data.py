import json

JSON_PATH = '/home/gustavo/Documents/Study/005_Python_General/github/python_practice/13_100_days_of_code/Day_31_to_40/Day_35/lesson_01_recap/four_days_forecast.json'

with open(JSON_PATH, 'r') as file:
    data = json.load(file)


# for i in data['list']:
#     if data['list'][0]['weather'][0]['id'] < 800:
#         print('get an umbrella')


#print(data['list'][0]['weather'][0]['id'])


will_rain = False

for hour_data in data['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella") 