import os

import requests

USERNAME = "jellef"
TOKEN = os.environ.get("PIXELA_API_TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# user created
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_entpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_entpoint, json=graph_config, headers=headers)
print(response.text)
