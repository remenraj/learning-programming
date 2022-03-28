# Musical Timemachine Project
# Scrapes the top 100 songs from Billboard.com at a given time and adds them into your spotify playlist

import requests, os, spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
from datetime import datetime



# <-------------------getting the date from user--------------------------------------------------------------------------------->
# get the date and verify it is valid
is_valid_date = False
while not is_valid_date:
    input_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    try:
        year, month, day = input_date.split('-')
    except ValueError:
        print("Invalid date format. Please try again.")
        is_valid_date = False
    else:

        try:
            datetime(int(year), int(month), int(day))
        except ValueError:
            print("Invalid date format. Please try again.")
            isValidDate = False
        else:
            is_valid_date = True


# <------------Scraping the billboard top 100----------------------------------------------------------------------------------->
# scraping the top 100 songs from Billboard.com at a given time
print("Scraping the Billboard for top songs")
BILLBOARD_URL = (
    r"https://www.billboard.com/charts/hot-100/" + input_date
)  

# get the html from the url
billboard_response = requests.get(BILLBOARD_URL)
billboard_response.raise_for_status()
billboard_html = billboard_response.text
# with open("billboard.html", "w") as file:
#     file.write(billboard_html)

# create a BeautifulSoup object
billboard_soup = BeautifulSoup(billboard_html, "html.parser")

# finding the 100 song titles using the css selector
song_titles_tag = billboard_soup.select(selector="li ul li h3")
song_titles = [song.getText().strip("\n\t") for song in song_titles_tag]

# # writing the song titles to a file
# with open("songs.txt", "w") as file:
#     # converting the list into a string joined by newline
#     file.write("\n".join(song_titles))


# <---------Authentication with Spotify---------------------------------------------------------------------------------------->

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URL = r"https://example.com/"

# if the user has not authorized the app yet, the following will redirect to the spotify authorization page and ask for permission
# copy the redirect url from the browser and paste it in the terminal
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=REDIRECT_URL,
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path=r"learning-programming\Python\51-100\54-musical-timemachine-project\token.txt",
    )
)

user_id = sp.current_user()["id"]

# getting the song uris from the spotify api
song_uris = []
for song in song_titles:
    track_response = sp.search(q=f"track:{song} year:{year}", type="track", limit = 1, market="IN", offset=0)
    
    try:
        uri = track_response["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify/Not available at your location. Skipped.")


# <---------Creating and Adding to Spotify Playlist----------------------------------------------------------------------------->
# creating a new playlist and retrieving the playlist id
playlist = sp.user_playlist_create(user=user_id, name=f"{input_date} Billboard 100", public=False)
playlist_id = playlist["id"]

# adding the list of songs to the playlist by using the uri of the songs
sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=song_uris, position=None)
