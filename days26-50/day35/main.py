import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPEN_WEATHER_MAP_API_KEY")
LAT = 40.4258686
LON = -86.9080655
account_sid = "AC6b5d19d6a2400792fbb01b4fa5afd74b"
auth_token = os.getenv("TWILLIO_AUTH_TOKEN")


def get_weather_data(url, params):
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def check_rain_forecast(hourly_data):
    for hour_data in hourly_data:
        if int(hour_data["weather"][0]["id"]) < 700:
            return True
    return False


def send_sms(message_text):
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_=os.getenv("TWILLIO_PHONE_NUMBER"),
        body=message_text,
        to=os.getenv("MY_PHONE_NUMBER")
    )
    print(message.status)


def main():
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q=West%20Lafayette,In,USA&appid={API_KEY}"
    weather_url = f"https://api.openweathermap.org/data/2.5/onecall"

    weather_params = {
        "lat": LAT,
        "lon": LON,
        "appid": API_KEY,
        "exclude": "current,minutely,daily"
    }

    weather_data = get_weather_data(weather_url, weather_params)
    hourly_data = weather_data["hourly"][:11]

    will_rain = check_rain_forecast(hourly_data)

    if will_rain:
        send_sms("It's going to rain today. Remember to bring an umbrella. ☔️")
    else:
        send_sms("You're good – no rain today!")


if __name__ == "__main__":
    main()
