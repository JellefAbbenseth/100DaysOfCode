import ssl

import requests

MY_LAT = 52.513550
MY_LNG = 13.387871
SUN_API_PATH = "https://api.sunrise-sunset.org/json"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get(SUN_API_PATH, params=parameters, verify=ssl.CERT_NONE)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

