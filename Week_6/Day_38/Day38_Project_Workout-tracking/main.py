import datetime
import os

import requests

APP_ID = os.environ.get("NUTRITION_ID")
API_KEY = os.environ.get("NUTRITION_KEY")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

# gender = input("Please type in your gender (male/female): ")
# weight = float(input("Please type in your weight (ex. 72.5): "))
# height = float(input("Please type in your height in cm (ex. 167.64): "))
# age = int(input("Please type in your age (ex. 30): "))
# workout_text = input("Please type in your exercise (ex. ran 3 miles): ")
# print(f"Gender: {gender},\nWeight: {weight}\nHeight: {height}\nAge: {age}")

# Examle:
gender = "female"
weight = 72.5
height = 167.64
age = 30
workout_text = "ran 3 miles"

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

date = datetime.datetime.now()
formatted_date = date.strftime("%d/%m/%Y")

headers_sheety = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {SHEETY_TOKEN}",
}

# Todo: Save data to sheety
