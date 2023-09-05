from typing import Dict
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()


def get_spotify_client() -> spotipy.Spotify:
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=os.getenv('spotify_client_id'),
        client_secret=os.getenv('spotify_client_secret'),
        redirect_uri='http://localhost',
        scope='playlist-modify-private',
        cache_path='token.txt',
        show_dialog=True
    ))


def url_construct() -> str:
    year = input("Give us a date to look at the top song of (yyyy-mm-dd): ")
    return f"https://www.billboard.com/charts/hot-100/{year}"


def get_songs(uri) -> Dict[str, str]:
    res = requests.get(uri)
    soup = BeautifulSoup(res.text, "html.parser")

    top_100_songs = soup.select('li ul li h3')
    top_100_artists = soup.find_all(name='span', class_='u-max-width-330')

    return {song.getText().strip(): artist.getText().strip() for song, artist in zip(top_100_songs, top_100_artists)}


def get_songs_uri(songs_artists: Dict[str, str], sp: spotipy.Spotify) -> list:
    uris = []

    for song, artist in songs_artists.items():
        result = sp.search(q=f'track:{song} artist:{artist}', type='track')
        try:
            uri = result['tracks']['items'][0]['uri']
            uris.append(uri)
        except IndexError:
            print(f"{song} by {artist} not found")
        finally:
            print(f"{len(uris)} out of {len(songs_artists)} found")

    return uris


def create_and_add_playlist(url: str, songs: list, sp: spotipy.Spotify):
    user_id = sp.current_user()["id"]
    title = f'{url.split("/")[-1]} Billboard 100'

    playlist = sp.user_playlist_create(user=user_id, name=title, public=False)
    sp.playlist_add_items(playlist['id'], songs, position=None)

    print(f"New playlist '{title}' successfully created on Spotify!")


if __name__ == '__main__':
    sp = get_spotify_client()
    url = url_construct()
    songs_and_artists = get_songs(url)
    songs_uris = get_songs_uri(songs_and_artists, sp)
    create_and_add_playlist(url=url, songs=songs_uris, sp=sp)
