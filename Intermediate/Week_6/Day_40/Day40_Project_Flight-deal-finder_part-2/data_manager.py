import json
import os

import requests


def save_users_data():
    users_data = {
        'users': [
            {"firstName": "Test", "lastName": "Tester", "Email": "test@tester.com"},
            {"firstName": "Test2", "lastName": "Tester2", "Email": "test2@tester2.com"},
        ]
    }
    with open("users_data.json", "w") as users_data_file:
        json.dump(users_data, users_data_file)


class DataManager:
    SHEETY_ID = os.environ.get("SHEETY_ID")
    SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
    SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_ID}/flightDeals/prices"

    def __init__(self):
        self.city = ""
        self.iata_code = ""
        self.lowest_price = 0
        self.data = self.get_flight_deals_data()
        self.users = self.get_users_data()

        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.SHEETY_TOKEN}",
        }

    def save_sheety_data(self):
        response = requests.get(url=self.SHEETY_ENDPOINT, headers=self.headers)
        self.data = response.json()
        # print(self.data)
        with open("flight_deals.json", "w") as flight_deals_file:
            json.dump(self.data, flight_deals_file)

    @staticmethod
    def get_flight_deals_data():
        try:
            with open("flight_deals.json", "r") as flight_deals_file:
                data = json.load(flight_deals_file)
                # print(data)
            return data
        except FileNotFoundError:
            print("File doesn't exist, please use save_sheety_data once!")

    @staticmethod
    def get_users_data():
        try:
            with open("users_data.json", "r") as users_data_file:
                data = json.load(users_data_file)
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

    def save_new_user_data(self, first_name: str, last_name: str, mail: str):
        try:
            with open("users_data.json", "w") as users_data_file:
                self.users["users"].append({
                    "firstName": first_name,
                    "lastName": last_name,
                    "Email": mail,
                })
                json.dump(self.users, users_data_file)
        except FileNotFoundError:
            print("File doesn't exist, please use save_users_data once!")

    def get_data(self):
        return self.data["prices"]

    def get_users(self):
        return self.users["users"]
