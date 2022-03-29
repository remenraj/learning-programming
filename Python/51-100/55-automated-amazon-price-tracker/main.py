# Automated amazon price tracker: Alerts user via email when the price is dropped below a certain threshold

from numpy import product
import requests
from bs4 import BeautifulSoup
import re, smtplib, os

# import lxml


# <-------Using BeautifulSoup to scrape the product price------------------------------------------------------------>

PRODUCT_URL = r"https://www.amazon.in/Store2508%C2%AE-Quality-FIBREGLASS-Mosquito-Installation/dp/B07GZTJK2M"

# headers are required to retrieve the html data from amazon website
# You can see your browser headers by going to this website: http://myhttpheader.com/
headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
}

# getting product page html
amazon_response = requests.get(url=PRODUCT_URL, headers=headers)
amazon_response.raise_for_status()
product_html = amazon_response.text
# with open("amazon.html", "w", encoding="utf-8") as file:
#     file.write(product_html)

# getting the current price of the product
product_soup = BeautifulSoup(product_html, "lxml")
price_tag = product_soup.find(name="span", class_="a-offscreen").getText()

# using regular expression to extract the price and converting into a floating point value
price_regex = re.compile(r"\d+.\d+")
price = float(price_regex.search(price_tag).group())
print(price)

# <-------Email alert when the price is below preset value------------------------------------------------------------>

PRESET_PRICE = 500.0

if price < PRESET_PRICE:
    
    EMAIL = os.environ.get("EMAIL")
    EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL, # sending email to the user itself
            msg=f"Subject: Amazon Price Alert\n\nPrice: {price_tag}\nLink:{PRODUCT_URL}".encode("utf-8"),
        )
    print("Email sent")
