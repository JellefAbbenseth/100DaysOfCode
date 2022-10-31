import random


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    # Class Search API needs private data, so I don't use it, will use random data
    def __init__(self):
        self.city_list = [
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
        self.random_price = []
        self.lower_limit = 30
        self.upper_limit = 600

    def get_flight_prices(self):
        for i in range(len(self.city_list)):
            self.random_price.append(random.randint(self.lower_limit, self.upper_limit))
        return self.random_price
