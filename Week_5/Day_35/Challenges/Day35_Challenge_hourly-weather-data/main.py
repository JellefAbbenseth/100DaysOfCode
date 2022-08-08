# API_KEY only activated during the challenge
import requests

API_KEY = "b28794401acad3b900530ffb25ff0e92"
MY_LAT = 52.513550
MY_LONG = 13.387871
RAINY_LAT = 46.607771388122394
RAINY_LONG = 23.55816366263232

API_WEATHER = "https://api.openweathermap.org/data/2.5/onecall"
PARAMETER = {
    "lat": RAINY_LAT,  # Pădureni 407209 Rumänien   MY_LAT,
    "lon": RAINY_LONG,  # MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}


# Challenge get data and search hourly forecast
def get_onecall_data():
    response = requests.get(url=API_WEATHER, params=PARAMETER)
    response.raise_for_status()
    weather_data = response.json()
    # with open("weather_data_response.json", "w") as file:
    #     file.write(str(response.json()))
    print(weather_data)
    twelve_hour_data = weather_data["hourly"][:12]
    print(twelve_hour_data)
    for i in range(len(twelve_hour_data)):
        for j in range(len(twelve_hour_data[i]["weather"])):
            print(twelve_hour_data[i]["weather"][j]["id"])
            if twelve_hour_data[i]["weather"][j]["id"] < 700:
                print("Bring an Umbrella")
                return


get_onecall_data()
