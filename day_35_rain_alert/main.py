# latitude and longitude from https://www.latlong.net/
# weather from https://openweathermap.org/api
# json viewer https://jsonviewer.stack.hu/

# https://api.openweathermap.org/data/2.5/weather?q=Edinburgh,UK&appid=35bc295c76b70e156cac92a9b577cecf
# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}

import requests
from smsService import SmsService

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "35bc295c76b70e156cac92a9b577cecf"
LAT = 56.03
LON = -3.41


def get_JSON_response():
    request = {
        "lat": LAT,
        "lon": LON,
        "cnt": 8,
        "units": "metric",
        "appid": API_KEY,
    }

    response = requests.get(OWM_ENDPOINT, params=request)
    print(f"Response Status: {response.status_code}")
    response.raise_for_status()
    json = response.json()
    return json


def search_for_rain(json):
    weather = {item["dt_txt"]:item["weather"][0]["main"] for item in json["list"] if item["weather"][0]["id"] < 700}
    return weather


def weather_forcasts(json):
    return {item["dt_txt"]: {"weather": item["weather"][0]["description"], "temp_max": item["main"]["temp_max"], "temp_min":item["main"]["temp_min"]} for item in json["list"]}


def build_message(forecasts):
    message = "Your weather forecast for the next 24 hours:\n\n"
    for (key, value) in forecasts.items():
        message += f"{key}: Weather: {value["weather"]}, Temp: {value["temp_min"]}C - {value["temp_max"]}C\n"
    return message


json_values = get_JSON_response()
print(json_values)
# rain_forecasts = search_for_rain(json_values)
# print(rain_forecasts)
forecasts = weather_forcasts(json_values)
print(forecasts)
message = build_message(forecasts)
print(message)

service = SmsService()
service.send_message("+447773904375", message)

# if len(rain_forecasts) > 0:
#     service = SmsService()
#     service.send_message("+447773904375", "Bring an Umbrella")

