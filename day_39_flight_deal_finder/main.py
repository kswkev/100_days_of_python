# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
import datetime

LONDON = "LON"

datamanager = DataManager()
flight_search = FlightSearch()

def update_missing_iata_codes(records):
    print(f"Detected {len(records)} cities without IATA codes")
    for record in records:
        iata_code = flight_search.get_city_code(record["city"])
        record["iataCode"] = iata_code
        datamanager.update_record(record)


stored_data = datamanager.get_stored_flight_data()

missing_iata_codes = [item for item in stored_data if item["iataCode"] == ""]
if len(missing_iata_codes) > 0:
    update_missing_iata_codes(missing_iata_codes)

from_date = datetime.datetime.now() + datetime.timedelta(days = 2)
to_date = datetime.datetime.now() + datetime.timedelta(days = 180)
flight_search.find_flights_to(LONDON, "PAR", from_date, to_date, 7, 28)