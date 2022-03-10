#! usr/bin/env python3
# Stock News Alert app
# Sends you an sms when the percentage change in stock price is above or below a certain threshold value in the last 2 days
import requests, os
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


def check_stock_price() -> float:
    """Returns the stock price percentage change in the last 2 days"""

    # "Alpha Vantage! Your dedicated access key is: 9677GUPR3EY72ISE"
    ALPHA_VANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
    ALPHA_VANTAGE_API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")

    stock_api_parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": ALPHA_VANTAGE_API_KEY,
    }

    stock_response = requests.get(ALPHA_VANTAGE_ENDPOINT, params=stock_api_parameters)
    stock_response.raise_for_status()

    stock_data = stock_response.json()

    # dictionary of past 100 daily stock data
    time_series_daily = stock_response.json()["Time Series (Daily)"]

    # converting the dictionary into a list of dictionary
    closing_price_list = [
        float(value["4. close"]) for (key, value) in time_series_daily.items()
    ]

    # calculating the price variation(increase or decrease in percentage)
    price_variation = (
        100 * (closing_price_list[0] - closing_price_list[1]) / closing_price_list[1]
    )

    return price_variation


def get_news() -> list:
    """Returns three articles in a list using the news api"""
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
    NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

    NEWS_PARAMETERS = {
        "qInTitle": STOCK,
        "apiKey": NEWS_API_KEY,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMETERS)
    news_response.raise_for_status()

    all_articles = news_response.json()["articles"]

    three_articles = all_articles[:3]

    return three_articles


if __name__ == "__main__":

    # get the percentage change in stock price
    percentage_change = check_stock_price()

    # symbol for showing increasing/decreasing in sms
    up_or_down = None
    if percentage_change > 0:
        up_or_down = "🔺"
    else:
        up_or_down = "🔻"

    # sending the text message if the stock price change is greater than 5%
    if abs(percentage_change) > 4:
        twilio_account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
        TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
        TWILIO_VIRTUAL_NUMBER = os.environ.get("TWILIO_VIRTUAL_NUMBER")
        TWILIO_VERIFIED_NUMBER = os.environ.get("TWILIO_VERIFIED_NUMBER")

        client = Client(twilio_account_sid, TWILIO_AUTH_TOKEN)

        # getting three articles
        articles = get_news()

        # formatting the articles
        formatted_messages = [
            f"{STOCK}: {up_or_down}{abs(round(percentage_change, 2))}%\nHeadline:{item['title']}\nBrief:{item['description']}"
            for item in articles
        ]
        print(formatted_messages)
        # sending the message
        for message in formatted_messages:
            message = client.messages.create(
                body=message, from_=TWILIO_VIRTUAL_NUMBER, to=TWILIO_VERIFIED_NUMBER
            )
