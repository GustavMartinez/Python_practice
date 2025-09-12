import requests
from datetime import datetime

pixela_endpoint = 'https://pixe.la/v1/users'

USERNAME = 'gustavomart'
TOKEN = "lkasdfpqwer9875afas"


user_params ={
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


graph_config = {
    "id": "graph1",
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}


headers = {
    "X-USER-TOKEN": TOKEN
}


# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

today = datetime(year=2025, month=9, day=10 )
# print(today.strftime("%Y%m%d"))


pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15",
}

# response = requests.post(url=pixel_creation, json=pixel_data, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"


response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)