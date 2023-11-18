import requests
from datetime import datetime

USERNAME = "[create any username]"
TOKEN = "[put any password you want]"
GRAPH = "graph1"


pixela_endpoint = "https://pixe.la/v1/users"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

header = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers= header)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{GRAPH}"


today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today?"),
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=header)
print(response.text)

pixel_update = f"{pixel_endpoint}/{today.strftime('%Y%m%d')}"

update_config = {
    "quantity": "50.9"
}

# response = requests.put(url=pixel_update, json=update_config, headers=header)
# print(response.text)

pixel_delete = f"{pixel_update}"

# response = requests.delete(url=pixel_delete, headers=header)
# print(response.text)
