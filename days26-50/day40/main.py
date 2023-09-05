from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

sheet = DataManager()


def new_user():
    print("Welcome to Jared's Flight Club.")
    print("We find the best flight deals and email you.")
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    email = input("What is your email? ")
    validation = input("Type your email again. ")

    if email == validation:
        user_info = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
            }
        }

        sheet.add_user(user_info)
    else:
        print("emails dont match")


def search():
    flight_search = FlightSearch()
    notification_manager = NotificationManager()

    for city in sheet.get_sheet_data():
        if city["iataCode"] == '':
            location = flight_search.search_city(city["city"])
            city["iataCode"] = location["locations"][0]["code"]
            sheet.update_city_code(city)

        flight = flight_search.search_flight_to(city["iataCode"])
        if flight and flight.price < city["lowestPrice"]:
            # notification_manager.send_sms(flight)
            print(flight)

answer = input("Do you want to signup or search?")
if answer == "signup":
    new_user()
if answer == "search":
    search()
