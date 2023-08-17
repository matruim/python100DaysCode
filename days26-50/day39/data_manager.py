import requests
from dotenv import load_dotenv

load_dotenv()


class DataManager:
    def __init__(self):
        self.get_url = "https://api.sheety.co/279e398dc3434f2d9e7d73294c68a4f9/flightDeals/prices"

    def get_sheet_data(self):
        res = requests.get(self.get_url)
        res.raise_for_status()
        return res.json()["prices"]

    def update_city_code(self, city):
        url = f"{self.get_url}/{city['id']}"
        params = {
            "price": {
                'iataCode': city["iataCode"],
            }
        }
        res = requests.put(url, json=params)
        res.raise_for_status()
        print(res.text)
