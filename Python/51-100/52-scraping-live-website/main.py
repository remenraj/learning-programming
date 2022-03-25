#! usr/bin/env python3

# Scraping a live website: https://news.ycombinator.com/

import requests
from bs4 import BeautifulSoup


website_response = requests.get("https://news.ycombinator.com/")
website_response.raise_for_status()

# saving the html of the website
yc_webpage = website_response.text

# # saving the html of the website in a file
# with open("yc_webpage.html", "w") as yc_webpage_file:
#     yc_webpage_file.write(yc_webpage)

# creating a soup object
yc_soup = BeautifulSoup(yc_webpage, "html.parser")
# print(yc_soup.title.text)

##################################################################################
# printing the title, link and upvote score of the first article in the website
article_tag = yc_soup.find(name="a", class_="titlelink")
article_text = article_tag.getText()
article_link = article_tag.get("href")
article_upvote = yc_soup.find(name="span", class_="score").getText()

print(article_text)
print(article_link)
print(article_upvote)

#####################################################################################
# printing the title, link and upvote score of all the articles in the home page
articles = yc_soup.find_all(name="a", class_="titlelink")

# getting all the texts and links
article_texts = []
article_links = []
for article_tag in articles:
    article_text = article_tag.getText()
    article_texts.append(article_text)

    article_link = article_tag.get("href")
    article_links.append(article_link)

# getting all the upvote texts and converting the text into ingeger score
article_upvotes = [
    int(article_upvote.getText().split()[0])
    for article_upvote in yc_soup.find_all(name="span", class_="score")
]

print(article_texts)
print(article_links)
print(article_upvotes)

# finding the article with maximum upvotes
max_index = article_upvotes.index(max(article_upvotes))
print(article_texts[max_index])
print(article_links[max_index])
print(article_upvotes[max_index])
