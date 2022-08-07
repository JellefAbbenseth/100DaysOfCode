import requests

QUESTION_DATA_API_URL = "https://opentdb.com/api.php"

PARAMETERS: dict[str, str | int] = {
    "amount": 10,
    "type": "boolean",
}


def get_data():
    response = requests.get(url=QUESTION_DATA_API_URL, params=PARAMETERS)
    response.raise_for_status()
    data_list = response.json()["results"]
    return data_list


question_data = get_data()
