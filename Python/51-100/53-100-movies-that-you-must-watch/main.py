# Scraping the 100 movies that you must watch from the webpage
# https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/

import requests
from bs4 import BeautifulSoup


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
MOVIES_FILE_DIR = (
    r"learning-programming\Python\51-100\53-100-movies-that-you-must-watch"
)


# Get the webpage
website_response = requests.get(URL)
website_response.raise_for_status()
webpage_html = website_response.text

# creating a soup object
movies_soup = BeautifulSoup(webpage_html, "html.parser")
# print(movies_soup.prettify())

# finding all the movie titles
movie_tag_list = movies_soup.find_all(name="h3", class_="title")

# creating a list of movie titles and reversing the order
movies_list = [movie_tag.getText() for movie_tag in movie_tag_list]
movies_list.reverse()
# another method for reversing a list: movies_list[::-1]
# print(movies_list)

# saving the list of movie names to a text file
with open(f"{MOVIES_FILE_DIR}\\100 Movies That You Must Watch.txt", "w") as movies_file:
    # converting the list into a string joined by newline
    movies_file.write("\n".join(movies_list))
