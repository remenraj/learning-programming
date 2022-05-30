# Program to get the price of a product from amazon

from bs4 import BeautifulSoup
import requests, re


def get_amazon_price(product_url):
    headers = {
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
    }
    response = requests.get(url=product_url, headers=headers)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")
    price_tag = soup.find(name="span", class_="a-offscreen").getText()

    price = float(re.sub(r"[^\d.]", "", price_tag))
    
    return price


if __name__ == "__main__":
    print(get_amazon_price("https://www.amazon.in/Automate-Boring-Stuff-Python-2nd-dp-1593279922/dp/1593279922"))