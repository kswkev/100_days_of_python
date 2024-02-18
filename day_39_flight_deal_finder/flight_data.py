class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(self):
        pass

    def parse_flight_data(self, returned_data):

        data = returned_data["data"][0]

        flight_data = {
            "city_code_to": data["cityTo"],
            "local_departure": data["local_departure"],
            "local_arrival": data["local_arrival"],
            "nights": data["nightsInDest"],
            "price": data["price"]
        }

        return flight_data