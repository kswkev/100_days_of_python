import requests
import os

ALPHAVANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
FUNCTION = "TIME_SERIES_DAILY"
DAILY_KEY = "Time Series (Daily)"


class StockService:

    def __init__(self):
        self.ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

    def get_last_x_days_for(self, days, company):
        response_json = self.get_response(company)
        values = [item for item in response_json[DAILY_KEY].values()]
        return values[0:days]

    def get_response(self, company):
        alpha_request = {
            "function": FUNCTION,
            "symbol": company,
            "apikey": self.ALPHAVANTAGE_API_KEY
        }

        response = requests.get(ALPHAVANTAGE_ENDPOINT, alpha_request)
        response.raise_for_status()
        response_json = response.json()
        return response_json
