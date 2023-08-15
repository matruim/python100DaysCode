import datetime
import requests
from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


def get_stock_price():
    res = requests.get(STOCK_ENDPOINT, params={
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_NAME,
        "outputsize": "compact",
        "datatype": "json",
        "apikey": os.getenv("ALPHAVANTAGE_API_KEY")
    })
    res.raise_for_status()
    first2pairs = [res.json()["Time Series (Daily)"][k] for k in sorted(res.json()["Time Series (Daily)"].keys())[:2]]
    yesterday = first2pairs[0]
    day_before_yesterday = first2pairs[1]
    print(yesterday)
    print(day_before_yesterday)
    delta = abs(float(yesterday["4. close"]) - float(day_before_yesterday["4. close"]))
    print(delta)
    percent = (delta / max(float(yesterday["4. close"]), float(day_before_yesterday["4. close"]))) * 100
    print("{:.2f}".format(percent))
    if percent >= 5:
        symbol = "🔺" if float(yesterday["4. close"]) > float(day_before_yesterday["4. close"]) else "🔻"
        get_news(symbol, "{:.2f}".format(percent))


def get_news(symbol, percent):
    res = requests.get(NEWS_ENDPOINT, params={
        "apiKey": os.getenv("NEWS_API_KEY"),
        "q":STOCK_NAME,
        "from": datetime.datetime.today() - datetime.timedelta(days=3)
    })
    res.raise_for_status()
    first_3_articles = res.json()["articles"][:3]
    print(first_3_articles)
    for article in first_3_articles:
        message = f"{STOCK_NAME}: {symbol}{percent}%\nHeadline: {article['title']}\nBrief: {article['description']}"
        print(message)


def send_sms(message_text):
    account_sid = "AC6b5d19d6a2400792fbb01b4fa5afd74b"
    auth_token = os.getenv("TWILLIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_=os.getenv("TWILLIO_PHONE_NUMBER"),
        body=message_text,
        to=os.getenv("MY_PHONE_NUMBER")
    )
    print(message.status)


get_stock_price()