import requests
from datetime import datetime

ISS_URL = "http://api.open-notify.org/iss-now.json"
SUNRISE_URL = "https://api.sunrise-sunset.org/json"

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude
ERROR_RANGE = 5

def get_iss_location():
    response = requests.get(url=ISS_URL)
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return iss_latitude, iss_longitude


def get_sunrise_sunset_hours(request):
    response = requests.get(SUNRISE_URL, params=request)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    return sunrise, sunset


#Your position is within +5 or -5 degrees of the ISS position.
def is_iss_overhead(iss_pos, my_pos, error_range):
    iss_lat = iss_pos[0]
    iss_lng = iss_pos[1]
    my_lat = my_pos[0]
    my_lng = my_pos[1]
    return ((my_lat - error_range) <= iss_lat <= (my_lat + error_range)
            and (my_lng - error_range) <= iss_lng <= (my_lng + error_range))

def is_night(night_hours, current_hour):
    return night_hours[0] >= current_hour or night_hours[1] <= current_hour

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

time_now = datetime.now().hour

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

iss_pos = get_iss_location()
my_pos = (MY_LAT, MY_LONG)
sun_rise_set = get_sunrise_sunset_hours(parameters)

if is_night(sun_rise_set, time_now) and is_iss_overhead(iss_pos, my_pos, ERROR_RANGE):
    print("over head")
