import os
from datetime import datetime

import requests


class News:
    def __init__(self, company_name: str):
        self.NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
        self.company_name = company_name.split(" ")
        self.API_NEWS = "https://newsapi.org/v2/top-headlines"
        self.first_day = str(datetime.now().date)
        self.articles = []

        self.PARAMETER = {
            "q": self.company_name[0],
            "from": self.first_day,
            "sortBy": "publishedAt",
            "apiKey": self.NEWS_API_KEY,
        }

    def get_news_data(self):
        response = requests.get(url=self.API_NEWS, params=self.PARAMETER)
        response_data = response.json()
        for i in range(3):
            self.articles.append({
                "Headline": response_data["articles"][i]["title"],
                "Brief": response_data["articles"][i]["description"]
            })
        return self.articles
