# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from data_manager import DataManager

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

