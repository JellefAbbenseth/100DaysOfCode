# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
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
    return [
        datetime.datetime(year=2022, month=month, day=day).strftime("%Y-%m-%d"),
        datetime.datetime(year=2022, month=month_end, day=day_end).strftime("%Y-%m-%d")
    ]


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

# for city in city_list:
#     data_manager.update_data(city[0], city[1])
# data_manager.save_updated_data()

flight_search = FlightSearch()
price_list = flight_search.get_flight_prices()
data_list = data_manager.get_data()

for i in range(len(price_list)):
    if price_list[i] < data_list[i]["lowestPrice"]:
        dates = random_dates()
        print(f"Low price alert! Only ${price_list[i]} to fly from Franfurt to {data_list[i]['city']}, "
              f"from {dates[0]} to {dates[1]}.")
        break
