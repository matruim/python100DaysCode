import datetime
import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWILIO_AUTH_TOKEN = os.getenv("TWILLIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILLIO_PHONE_NUMBER")
MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


def get_stock_price():
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "outputsize": "compact",
        "datatype": "json",
        "apikey": ALPHAVANTAGE_API_KEY
    }
    res = requests.get(STOCK_ENDPOINT, params=params)
    res.raise_for_status()
    time_series = res.json()["Time Series (Daily)"]
    recent_days = list(time_series.keys())[:2]
    (yesterday_close, day_before_yesterday_close) = [float(time_series[day]["4. close"]) for day in recent_days]
    delta = abs(yesterday_close - day_before_yesterday_close)
    percent = (delta / max(yesterday_close, day_before_yesterday_close)) * 100
    symbol = "🔺" if yesterday_close > day_before_yesterday_close else "🔻"

    if percent >= 5:
        get_news(symbol, "{:.2f}".format(percent))


def get_news(symbol, percent):
    params = {
        "apiKey": NEWS_API_KEY,
        "q": STOCK_NAME,
        "from": (datetime.datetime.today() - datetime.timedelta(days=3)).strftime('%Y-%m-%d')
    }
    res = requests.get(NEWS_ENDPOINT, params=params)
    res.raise_for_status()
    articles = res.json()["articles"][:3]
    for article in articles:
        message = f"{STOCK_NAME}: {symbol}{percent}%\nHeadline: {article['title']}\nBrief: {article['description']}"
        send_sms(message)


def send_sms(message_text):
    client = Client(TWILIO_AUTH_TOKEN, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        from_=TWILIO_PHONE_NUMBER,
        body=message_text,
        to=MY_PHONE_NUMBER
    )
    print(message.status)


get_stock_price()
