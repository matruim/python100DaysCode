from datetime import date
from dateutil.relativedelta import relativedelta
import os
import requests
from flight_data import FlightData

from dotenv import load_dotenv

load_dotenv()


class FlightSearch:

    def __init__(self):
        self.search_url = "https://api.tequila.kiwi.com/v2/search"
        self.location_url = "https://api.tequila.kiwi.com/locations/query"
        self.header = {"apikey": os.getenv("TEQUILA_KIWI_API_KEY")}
        today = date.today().strftime("%d/%m/%Y")
        six_months = (date.today() + relativedelta(months=6)).strftime("%d/%m/%Y")
        self.search_params = {
            "curr": "USD",
            "fly_from": "IND",
            "date_from": today,
            "date_to": six_months,
            "locale": "us",
            "max_stopovers": 2,
            "sort": "price",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
        }
        self.location_params = {
            "location_types": "city",
        }

    def search_flight_to(self, destination_airport):
        self.search_params["fly_to"] = destination_airport
        res = requests.get(self.search_url, params=self.search_params, headers=self.header)
        res.raise_for_status()
        try:
            data = res.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_airport}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["cityFrom"],
            origin_airport=data["flyFrom"],
            destination_city=data["cityTo"],
            destination_airport=data["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][len(data["route"])-1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data

    def search_city(self, city_name):
        self.location_params["term"] = city_name
        res = requests.get(self.location_url, params=self.location_params, headers=self.header)
        res.raise_for_status()
        return res.json()
