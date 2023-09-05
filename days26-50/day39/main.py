from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager


sheet = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

for city in sheet.get_sheet_data():
    if city["iataCode"] == '':
        location = flight_search.search_city(city["city"])
        city["iataCode"] = location["locations"][0]["code"]
        sheet.update_city_code(city)

    flight = flight_search.search_flight_to(city["iataCode"])
    if flight and flight.price < city["lowestPrice"]:
        notification_manager.send_sms(flight)
