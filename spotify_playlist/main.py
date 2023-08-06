from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
SPOTIFY_CLIENT = os.environ.get('SPOTIFY_CLIENT')
SPOTIFY_SECRET = os.environ.get('SPOTIFY_SECRET')
USER_ID = os.environ.get('SPOTIFY_USER_ID')
PLAYLIST_ID= os.environ.get('SPOTIFY_PLAYLIST_ID')

def search_song_id_on_spotify(song, year):
    try:
        search = sp.search(q=f'track:{song} year:{year}', type='track', limit=1)
        return search['tracks']['items'][0]['id']
    except IndexError:
        print(f'{song} not found on Spotify.')

##########################BILLBOARD 100 QUERY############################# 
date_for_billboard_query = input("Which year do you want to travel to? " 
                              "Type the date in this format YYYY-MM-DD:")

response = requests.get(f'{BILLBOARD_URL}{date_for_billboard_query}')
billboard_playlist = response.text

soup = BeautifulSoup(billboard_playlist, 'html.parser')

songs_tags = soup.select('div.o-chart-results-list-row-container ul li ul li h3#title-of-a-story')

songs = [song.getText(strip=True) for song in songs_tags]
#########################################################################

###########################SPOTIPY#######################################
#Spotify Scope to use to create a private playlist
scope = 'playlist-modify-private'
#Connection manager to Spotify
sp_auth = SpotifyOAuth(client_id=SPOTIFY_CLIENT, client_secret=SPOTIFY_SECRET,
                  redirect_uri='https://example.com', scope=scope, cache_path="./token.txt")
#Spotipy Client Module
sp = spotipy.Spotify(auth_manager=sp_auth)

# Get Token to Spotify from Spotipy
#print(sp_auth.get_access_token())
#Get User informations
#print(sp.current_user())

 
# TODO : get songs URIs from songs array
year = date_for_billboard_query.split('-')[0]

#songs_uris = [sp.search(q=f'track:{song} year:{year}', type='track', limit=1)['tracks']['items'][0]['id'] for song in songs]
songs_uris = [search_song_id_on_spotify(song, year) for song in songs if search_song_id_on_spotify(song, year) is not None]

# TODO : create a playlist from user input
playlist = sp.user_playlist_create(user=USER_ID, name=f'{date_for_billboard_query} Billboard 100', public=False)
#print(sp.user_playlists(user=USER_ID))

# TODO : for each song in songs array, add to playlist
sp.playlist_add_items(playlist_id=playlist['id'], items=songs_uris)

