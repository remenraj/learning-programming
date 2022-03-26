#! usr/bin/env python3

# Exploring BeautifulSoup
from bs4 import BeautifulSoup

# import lxml   # when using xml


try:
    WEBSITE_FILE_DIR = (
        r"learning-programming\Python\51-100\51-exploring-beautifulSoup\website.html"
    )
except FileNotFoundError:
    print("File not found")


with open(WEBSITE_FILE_DIR, "r") as website_file:
    contents = website_file.read()

# creating a soup object
soup = BeautifulSoup(
    contents, "html.parser"
)  # "html.parser" is the parser. Other parsers are "lxml" and "xml"

# printing the title tag
print(soup.title)

# printing the title tag name
print(soup.title.name)

# printing the title tag string
print(soup.title.string)

# printing the first paragraph tag
print(soup.p)

# printing the soup object prettified
print(soup.prettify())

# printing the first anchor tag
print(soup.a)

# printing all the anchor tags in the soup object in a list
all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# printing all the anchor texts
for anchor_tag in all_anchor_tags:
    # printing the anchor text
    print(anchor_tag.getText())
    # print(anchor_tag.string)

    # printing the links
    print(anchor_tag.get("href"))

# finding a heading with the id of "head"
heading = soup.find(name="h1", id="name")
print(heading)

# finding an attribute with the class of "heading"
# here 'class_' is used instead of 'class'
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
print(section_heading.getText())  # printing the heading text
print(section_heading.get("class"))  # printing the heading class
print(section_heading.get("id"))  # printing the heading id


### css selectors
# finding an url inside some attributes. here the link is inside p and a tags
# select_one is used to find the first url
# select is used to find all the urls
company_url = soup.select_one("p a")
print(company_url)
print(company_url.getText())

# select can also be used to find id, class, href, text, etc.
# id
name = soup.select_one(selector="#name")
print(name)

# class
headings = soup.select(".heading")
print(headings)
