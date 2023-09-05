import os
from flight_data import FlightData
from twilio.rest import Client


class NotificationManager:

    def __init__(self):
        self.url = ""
        self.sid = os.getenv("TWILLIO_SID")
        self.token = os.getenv("TWILLIO_AUTH_TOKEN")
        self.apiphone = os.getenv("TWILLIO_PHONE_NUMBER")
        self.myphone = os.getenv("MY_PHONE_NUMBER")

    def send_sms(self, message_text:FlightData):
        client = Client(self.sid, self.token)
        message = client.messages.create(
            from_=self.apiphone,
            body=message_text.__str__(),
            to=self.myphone
        )
        print(message.status)