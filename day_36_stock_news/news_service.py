import datetime as dt
import requests
import os

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


class NewsService:

    def __init__(self):
        self.NEWS_API_KEY = os.getenv("NEWS_API_KEY")

    def get_last_x_days_news_for_company(self, days, company_name):
        date_x_days_ago = str((dt.datetime.today() - dt.timedelta(days=days)).date())

        news_request = {
            "q": company_name,
            "from": date_x_days_ago,
            "sortBy": "publishedAt",
            "searchIn": "title",
            "language": "en",
            "apiKey": self.NEWS_API_KEY,
        }

        response = requests.get(NEWS_ENDPOINT, news_request)
        response.raise_for_status()
        response_json = response.json()
        return response_json

    def return_last_x_articles(self, amount, json):
        values = [item for item in json["articles"]]
        return values[0:amount]

    def format_data(self, data):
        return [{'title': item['title'], 'author': item['author'], 'url': item['url']} for item in data]