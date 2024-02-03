country = input("Add country name: ") # Add country name
visits = int(input("Number of visits: ")) # Number of visits
list_of_cities = eval(input("create list from formatted string: ")) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log.

def add_new_country(country, visits, list_of_cities):
    country_details = {
        "country": country,
        "visits": visits,
        "cities": list_of_cities,
    }
    travel_log.append(country_details)


# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")