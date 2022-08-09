# API_KEY only activated during the challenge
import os

import requests
API_KEY = os.environ.get("OWN_API_KEY")
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
    for hour_data in twelve_hour_data:
        for hourly_weather_data in hour_data["weather"]:
            if int(hourly_weather_data["id"]) < 700:
                print("Bring an Umbrella")
                return


get_onecall_data()
