import json
import os

import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    SHEETY_ID = os.environ.get("SHEETY_ID")
    SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
    SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_ID}/flightDeals/prices"

    def __init__(self):
        self.city = ""
        self.iata_code = ""
        self.lowest_price = 0
        self.data = self.get_flight_deals_data()

        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.SHEETY_TOKEN}",
        }

    # Not using sheety because of api limitations!! -> saved to flight deals.json
    def save_sheety_data(self):
        response = requests.get(url=self.SHEETY_ENDPOINT, headers=self.headers)
        self.data = response.json()
        print(self.data)
        with open("flight_deals.json", "w") as flight_deals_file:
            json.dump(self.data, flight_deals_file)

    @staticmethod
    def get_flight_deals_data():
        try:
            with open("flight_deals.json", "r") as flight_deals_file:
                data = json.load(flight_deals_file)
                print(data)
            return data
        except FileNotFoundError:
            print("File doesn't exist, please use save_sheety_data once!")

    def update_data(self, city: str, iata_code: str):
        for price in self.data["prices"]:
            if price["city"] == city:
                price["iataCode"] = iata_code
                return

    def save_updated_data(self):
        try:
            with open("flight_deals.json", "w") as flight_deals_file:
                json.dump(self.data, flight_deals_file)
        except FileNotFoundError:
            print("File doesn't exist, please use save_sheety_data once!")

    def get_data(self):
        return self.data["prices"]
