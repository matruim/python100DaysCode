import requests
from dotenv import load_dotenv

load_dotenv()


class DataManager:
    def __init__(self):
        self.base_url = "https://api.sheety.co/279e398dc3434f2d9e7d73294c68a4f9/flightDeals"
        self.user_url = f"{self.base_url}/users"
        self.get_url = f"{self.base_url}/prices"

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

    def add_user(self, user_info):
        res = requests.post(self.user_url, json=user_info)
        res.raise_for_status()
        print("your in the club.")