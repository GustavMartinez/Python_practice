# Working with APIs

# endpoint = Location of the data (url)

import requests

response = requests.get(url='http://api.open-notify.org/iss-now.json')

# print(response)
# print(response.status_code)

response.raise_for_status() # Important to see if there is an error

data = response.json()['iss_position']['longitude'] # Accessing the longitude from the file

longitude = response.json()['iss_position']['longitude']
latitude = response.json()['iss_position']['latitude']

position = (longitude, latitude)


print(data)
print(position)