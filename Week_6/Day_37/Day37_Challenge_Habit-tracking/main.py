import os

import requests
from datetime import datetime

USERNAME = "jellef"
TOKEN = os.environ.get("PIXELA_API_TOKEN")
GRAPH_ID = "graph1"

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
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# graph created
# response = requests.post(url=graph_entpoint, json=graph_config, headers=headers)
# print(response.text)

post_value_entpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2022, month=8, day=12)
formatted_day = today.strftime("%Y%m%d")

pixel_data = {
    "date": formatted_day,     # date in yyyMMdd
    "quantity": "4.6",         #
}

# response = requests.post(url=post_value_entpoint, json=pixel_data, headers=headers)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_day}"

pixel_update_data: dict[str, str] = {
    "quantity": "6.4",
}

# response = requests.put(url=update_endpoint, json=pixel_update_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{formatted_day}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
