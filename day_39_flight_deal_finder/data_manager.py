import os
import requests
from requests.auth import HTTPBasicAuth


class DataManager:
    SHEETY_ENDPOINT = "https://api.sheety.co/eb2bf31ecaeb35baa28d510e9946a898/flightDeals/prices"

    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_AUTH_PASSWORD = os.getenv("SHEETY_AUTH_PASSWORD")
        self.SHEETY_AUTH_USERNAME = os.getenv("SHEETY_AUTH_USERNAME")

    def get_stored_flight_data(self):
        print("Fetching records from Flight Deals spreadsheet")
        basic = HTTPBasicAuth(self.SHEETY_AUTH_USERNAME, self.SHEETY_AUTH_PASSWORD)
        response = requests.get(self.SHEETY_ENDPOINT, auth=basic)
        response.raise_for_status()
        json = response.json()
        records = [item for item in json["prices"]]
        print(f"{len(records)} records found")
        return records

    def update_record(self, record):
        print(f"Updating {record["city"]} IATA code to {record["iataCode"]}")
        new_data = {
            "price": {
                "iataCode": record["iataCode"]
            }
        }

        basic = HTTPBasicAuth(self.SHEETY_AUTH_USERNAME, self.SHEETY_AUTH_PASSWORD)
        response = requests.put(f"{self.SHEETY_ENDPOINT}/{record["id"]}", auth=basic, json=new_data)
        response.raise_for_status()