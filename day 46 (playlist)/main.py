from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


SPOTIFY_ID = '1ebef0bbc10342c3854f22baf33f2031'
SPOTIFY_SECRET = 'a88c69455ae5413ab9000cad679264fb'
SPOTIPY_REDIRECT_URI = 'http://example.com'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope='playlist-modify-private',
        redirect_uri=SPOTIPY_REDIRECT_URI,
        client_id=SPOTIFY_ID,
        client_secret=SPOTIFY_SECRET,
        show_dialog=True,
        cache_path='token.txt'
    )
)

user_id = sp.current_user()['id']


user_date = input('Which year would you like to travel to? Type in this format YYYY-MM-DD: ')
url = f'https://www.billboard.com/charts/hot-100/{user_date}/'

response = requests.get(url)
html_data = response.text
soup = BeautifulSoup(html_data, 'html.parser')

song_titles = soup.select(".o-chart-results-list__item h3.c-title")

titles_list = [title.getText().strip() for title in song_titles]
# print(titles_list)

year = user_date.split("-")[0]

uris_songs = []

for title in titles_list:
    result = sp.search(q=f"track:{title} year:{year}", type='track')
    # print(result)
    try:
        uri = result['tracks']['items'][0]['uri']
        uris_songs.append(uri)
    except IndexError:
        print(f"{title} doesn't exist! Skipped")


play_list = sp.user_playlist_create(user=user_id, name=f"{user_date} Billboard 100", public=False, description=f"TOP 100 song of {uris_songs}")

play_list_id = play_list['id']

sp.playlist_add_items(playlist_id=play_list_id, items=uris_songs, position=None)