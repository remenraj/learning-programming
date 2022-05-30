# Web pages are plaintext files formatted as HTML.
# HTML can be parsed with the BeautifulSoup module.
# BeautifulSoup is imported with the name bs4.
# Pass the string with the HTML to the bs4. BeautifulSoup() function to get a Soup object.
# The Soup object has a select() method that can be passed a string of the CSS selector for an HTML tag.
# You can get a CSS selector string from the browser's developer tools by right-clicking the element and selecting Copy CSS Path.
# The select() method will return a list of matching Element objects.

# install beautiful soup: pip install beautifulsoup4

import bs4, requests


amazon_url = (
    "https://www.amazon.in/Automate-Boring-Stuff-Python-2nd-dp-1593279922/dp/1593279922"
)

headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
}

response = requests.get(url=amazon_url, headers=headers)
response.raise_for_status()

soup = bs4.BeautifulSoup(response.text, "html.parser")  # parse the HTML


print(soup.select("#price")[0].getText())  # get the price])
