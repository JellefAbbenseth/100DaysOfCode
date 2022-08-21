import datetime
import random

from data_manager import DataManager
from flight_search import FlightSearch


def random_dates():
    day = random.randint(1, 30)
    month = random.randint(5, 12)
    if (day + 14) > 30:
        day_end = (day + 14) % 30
        if month + 1 == 13:
            month_end = 1
        else:
            month_end = month + 1
    else:
        day_end = day + 14
        month_end = month
    return [
        datetime.datetime(year=2022, month=month, day=day).strftime("%Y-%m-%d"),
        datetime.datetime(year=2022, month=month_end, day=day_end).strftime("%Y-%m-%d")
    ]


def register_user():
    while input("Do you want to register (true/false): ").lower() == "true":
        first_name = input("What is your first name?\n")
        last_name = input("What is your last name?\n")
        while True:
            email = input("What is your email?\n")
            check_email = input("Type your email again.\n")
            if email == check_email:
                break
            else:
                print("Something wrong, please try again, the email addresses should be identical!")

        data_manager.save_new_user_data(first_name, last_name, email)


print("Welcome to the Safer's Flight Club.")
print("We find the best flight deals and email you.")
city_list = [
    ["Paris", "PAR"],
    ["Berlin", "BER"],
    ["Tokyo", "TYO"],
    ["Sydney", "SYD"],
    ["Istanbul", "IST"],
    ["Kuala Lumpur", "KUL"],
    ["New York", "NYC"],
    ["San Francisco", "SFO"],
    ["Cape Town", "CPT"]
]

data_manager = DataManager()
# data_manager.save_sheety_data() -> free sheety api has limitations, therefore data is saved to flight_deals.json
# data_manager.save_users_data()

# for city in city_list:
#     data_manager.update_data(city[0], city[1])
# data_manager.save_updated_data()

register_user()

flight_search = FlightSearch()
price_list = flight_search.get_flight_prices()
data_list = data_manager.get_data()

for i in range(len(price_list)):
    if price_list[i] < data_list[i]["lowestPrice"]:
        dates = random_dates()
        print(f"Low price alert! Only ${price_list[i]} to fly from Franfurt to {data_list[i]['city']}, "
              f"from {dates[0]} to {dates[1]}.")
