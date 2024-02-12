import requests
import os
import datetime as dt
from requests.auth import HTTPBasicAuth

NUTRITIONIX_APP_ID = os.getenv("NUTRITIONIX_APP_ID")
NUTRITIONIX_APP_KEY = os.getenv("NUTRITIONIX_APP_KEY")
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/eb2bf31ecaeb35baa28d510e9946a898/myWorkouts/workouts"
SHEETY_AUTH_PASSWORD = os.getenv("SHEETY_AUTH_PASSWORD")
SHEETY_AUTH_USERNAME = os.getenv("SHEETY_AUTH_USERNAME")

WEIGHT_KG = 89
HEIGHT_CM = 180
AGE = 43


def get_exercise_data(query):
    header = {
        "x-app-id": NUTRITIONIX_APP_ID,
        "x-app-key": NUTRITIONIX_APP_KEY
    }

    request = {
        "query": query,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE
    }

    response = requests.post(url=NUTRITIONIX_ENDPOINT, json=request, headers=header)
    response.raise_for_status()
    response_json = response.json()
    exercises = [{"exercise": item["user_input"], "duration": item["duration_min"], "calories": item["nf_calories"]} for item in response_json["exercises"]]
    return exercises


def update_spreadsheet(data):
    formatted_date = dt.datetime.now().strftime("%d/%m/%Y")
    formatted_time = dt.datetime.now().strftime("%H:%M:%S")

    for exercise in data:
        add_row_request = {
            "workout": {
                "date": formatted_date,
                "time": formatted_time,
                "exercise": exercise["exercise"],
                "duration": exercise["duration"],
                "calories": exercise["calories"]
            }
        }

        basic = HTTPBasicAuth(SHEETY_AUTH_USERNAME, SHEETY_AUTH_PASSWORD)
        response = requests.post(SHEETY_ENDPOINT, json=add_row_request, auth=basic)
        response.raise_for_status()


query_text = input("Tell me which exercises you did: ")
exercise_data = get_exercise_data(query_text)
update_spreadsheet(exercise_data)


