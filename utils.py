import requests
from url_json import JSON_APP_URL


def load_data():
    response = requests.get(JSON_APP_URL)
    data = response.json()
    candidates = {}
    for i in data:
        candidates[i['id']] = i
    return candidates


load_data()
