import requests
import datetime as dt


parameters = {
    'lat': -19.917299, 
    'lng': -43.934559,
    'formatted': 0
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()

data = response.json()

# ['results'] first key, ['sunrise'] second key
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)




# adding the formatted parameter

time_now = dt.datetime.now()
print(time_now.hour)
