import datetime
import os
import requests

APP_ID = os.environ.get("NUTRITION_ID")
API_KEY = os.environ.get("NUTRITION_KEY")
SHEETY_ID = os.environ.get("SHEETY_ID")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_ID}/projectWorkout/workout"

# Examle:
# gender = "female"
# weight = 72.5
# height = 167.64
# age = 30
# workout_text = "ran 3 miles"

gender = input("Please type in your gender (male/female): ")
weight = float(input("Please type in your weight (ex. 72.5): "))
height = float(input("Please type in your height in cm (ex. 167.64): "))
age = int(input("Please type in your age (ex. 30): "))
workout_text = input("Please type in your exercise (ex. ran 3 miles): ")
print(f"Gender: {gender},\nWeight: {weight}\nHeight: {height}\nAge: {age}")


headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_config = {
    "query": workout_text,
    "gender": gender,
    "weight_kg": weight,
    "height_cm": height,
    "age": age,
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=exercise_config, headers=headers)
print(response.text)

nutrition_data = response.json()["exercises"]

for data in nutrition_data:
    exercise = data["name"]
    duration = int(round(data["duration_min"], 0))
    calories = int(round(data["nf_calories"], 0))

    date = datetime.datetime.now()
    formatted_date = date.strftime("%d/%m/%Y")
    formatted_time = date.strftime("%H:%M:%M")

    headers_sheety = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {SHEETY_TOKEN}",
    }

    body = {
        "workout": {
            "date": formatted_date,
            "time": formatted_time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
        }
    }

    response = requests.post(url=SHEETY_ENDPOINT, json=body, headers=headers_sheety)
    print(response.text)
