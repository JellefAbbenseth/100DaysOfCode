import os
import requests
import spotipy as spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

ID = os.environ["SPOTIFY_ID"]
SECRET = os.environ["SPOTIFY_SECRET"]
REDIRECT_URI = os.environ["SPOTIFY_REDIRECT"]
URL = "https://www.billboard.com/charts/hot-100/2000-08-12/"
SPOTIFY_O_AUTH = SpotifyOAuth(client_id=ID,
                              client_secret=SECRET,
                              redirect_uri=REDIRECT_URI,
                              scope="playlist-modify-private")

# date = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD:\n")

response = requests.get(URL)  # + date
billboard_web_page = response.text
# print(billboard_web_page)

soup = BeautifulSoup(billboard_web_page, "lxml")
song_titles = [song.getText().strip() for song in soup.select(".o-chart-results-list__item #title-of-a-story")]
print(song_titles)

sp = spotipy.Spotify(auth_manager=SPOTIFY_O_AUTH)

results = sp.current_user()
print(results)
user_id = results["id"]
print(user_id)

# ToDo: Finish step 4!
# 408. Step 4

results = sp.track(song_titles[0])
print(results)
