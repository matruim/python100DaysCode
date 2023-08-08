import datetime
import smtplib as smtp
import time

import requests
from dateutil.parser import parse
import pytz

MY_EMAIL = ""
MY_LAT = 40.440560129660945
MY_LONG = -86.9623479619754
EASTERN = pytz.timezone("US/Eastern")
FROM = {
    "email":"x@gmail.com",
    "pass": "",
    "host": "smtp.gmail.com"
}


def get_iss_location():
    url = "http://api.open-notify.org/iss-now.json"
    res = requests.get(url)
    res.raise_for_status()
    iss_position = res.json()["iss_position"]
    return {"lat": float(iss_position["latitude"]), "long": float(iss_position["longitude"])}


def get_sunrise_sunset_data(lat, long):
    url = "https://api.sunrise-sunset.org/json"
    params = {"lat": lat, "lng": long, "formatted": 0}
    res = requests.get(url, params=params)
    res.raise_for_status()
    return res.json()["results"]


def convert_to_datetime(time_str):
    return parse(time_str).replace(tzinfo=pytz.UTC)


def iss_near_me(tolerance=5):
    iss = get_iss_location()
    return abs(iss["lat"] - MY_LAT) <= tolerance and abs(iss["long"] - MY_LONG) <= tolerance


def is_dark(time=datetime.datetime.now().astimezone(EASTERN)):
    data = get_sunrise_sunset_data(MY_LAT, MY_LONG)
    sunrise = convert_to_datetime(data["sunrise"]).astimezone(EASTERN)
    sunset = convert_to_datetime(data["sunset"]).astimezone(EASTERN)
    return sunset < time or time < sunrise


def send_message(email):
    with smtp.SMTP(FROM["host"]) as connection:
        connection.starttls()
        connection.login(user=FROM["email"], password=FROM["pass"])
        connection.sendmail(
            from_addr=FROM["email"],
            to_addrs=email,
            msg="Subject: ISS Over Head\n\nGo outside and look up you should see the ISS"
        )


while True:
    time.sleep(60)
    if iss_near_me() and is_dark():
        send_message(MY_EMAIL)
