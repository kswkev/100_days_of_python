import requests

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    QUERY_END_POINT = "https://api.tequila.kiwi.com/locations/query"
    SEARCH_END_POINT = "https://api.tequila.kiwi.com/v2/search"

    def __init__(self):
        self.API_KEY = "y8vy6tOAX6iepgTEOJNQMiTj2iVnZ1_t"

    def get_city_code(self, city):
        print(f"Searching for location IATA code for {city}")

        header = {
            "apikey": self.API_KEY
        }

        request = {
            "term": city,
            "locale": "en-US",
            "location_types": "city",
            "limit": 10,
            "active_only": "true"
        }

        response = requests.get(self.QUERY_END_POINT, request, headers=header)
        response.raise_for_status()
        if len(response.json()["locations"]) > 0:
            code = response.json()["locations"][0]["code"]
            print(f"IATA code {code} found for city {city}")
            return code
        else:
            return ""

    def find_flights_to(self, source_city_iata, destination_city_iata, date_from, date_to, min_stay, max_stay):
        print(f"Search for flights from {source_city_iata} to {destination_city_iata}\n"
              f"with departure date between {date_from} and {date_to}")

        header = {
            "apikey": self.API_KEY
        }

        request = {
            "fly_from": source_city_iata,
            "fly_to": destination_city_iata,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": min_stay,
            "nights_in_dst_to": max_stay,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(self.SEARCH_END_POINT, request, headers=header)
        response.raise_for_status()
        print(response.json())