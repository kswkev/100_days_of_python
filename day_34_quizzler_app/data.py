import requests

def call_API(url, request):
    response = requests.get(url, params=request)
    response.raise_for_status()
    return response.json()

URL = "https://opentdb.com/api.php"

request = {
        "amount": 10,
        "type": "boolean"
    }


question_data = call_API(URL, request)["results"]
