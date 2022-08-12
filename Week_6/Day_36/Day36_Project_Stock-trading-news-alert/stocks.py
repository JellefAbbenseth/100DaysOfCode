import os
from datetime import datetime, timedelta

import requests


class Stocks:
    def __init__(self, stock_name: str, company_name: str, alert_price_difference: int):
        self.price_day_before_yesterday = 0.00
        self.price_yesterday = 0.00
        self.alert = False
        self.STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
        self.API_ALPHVANTAGE = "https://www.alphavantage.co/query"

        self.stock_name = stock_name
        self.company_name = company_name
        self.alert_price_difference = alert_price_difference
        self.price_difference = 0.00

        self.today = datetime.now().date()
        self.yesterday = str(self.today - timedelta(days=1))
        self.day_before_yesterday = str(self.today - timedelta(days=2))
        self.data_key_time_series_daily = "Time Series (Daily)"
        self.data_key_daily_closure = "4. close"

        self.PARAMETER = {
            "function": "TIME_SERIES_DAILY",  # Required
            "symbol": self.stock_name,  # Required
            "outputsize": "compact",  # Optional (compact or full)
            "datatype": "json",  # Optional (json or csv)
            "apikey": self.STOCK_API_KEY,  # Required
        }

    def get_stock_data(self):
        response = requests.get(url=self.API_ALPHVANTAGE, params=self.PARAMETER)
        time_series_daily = response.json()[self.data_key_time_series_daily]
        self.price_yesterday = float(time_series_daily[self.yesterday][self.data_key_daily_closure])
        self.price_day_before_yesterday = \
            float(time_series_daily[self.day_before_yesterday][self.data_key_daily_closure])
        self.price_difference: float = ((self.price_yesterday / self.price_day_before_yesterday) - 1) * 100
        if self.price_difference < -self.alert_price_difference or self.price_difference > self.alert_price_difference:
            self.alert = True

        return [self.price_yesterday, self.price_day_before_yesterday, self.price_difference, self.alert]
