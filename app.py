from flask import Flask, render_template
import random
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

app = Flask(__name__)

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


global_artist = ""
global_track = ""
global_genre = ""

@app.route('/')
def hello_world():
    
    fav_artists_name = ["J Cole", "Lil Wayne", "Drake"]
    fav_artists_id   = ["6l3HvQ5sa6mXTsMTB19rO5", "55Aa2cqylxrFIXC767Z865", "3TVXtAsR1Inumwj472S9r4"]
    random_number = random.randint(0,2)
    artist = fav_artists_id[random_number]
    name = sp.artist(artist)['name']
    
    random_number = random.randint(0,9)
    track_name = sp.artist_top_tracks(artist, "US")['tracks'][random_number]["name"]
    track_href=sp.artist_top_tracks(artist, "US")['tracks'][random_number]['external_urls']['spotify']
    track_id = sp.artist_top_tracks(artist, "US")['tracks'][random_number]['id']
    
    prev_url = sp.artist_top_tracks(artist, "US")['tracks'][random_number]["preview_url"]
    img_url = sp.artist_top_tracks(artist,"US")["tracks"][random_number]["album"]["images"][0]["url"]
    
    genre = sp.artist(artist)['genres'][0]
    
    global global_artist
    global_artist = artist
    
    global global_track
    global_track = track_id
    
    global global_genre
    global_genre = genre
    
    # print(name)
    # print(track_name)
    # print(prev_url)
    # print(img_url)
    return render_template(
        'index.html', 
        name = name,
        track = track_name,
        prev_url = prev_url,
        image=img_url,
        track_href = track_href,
        )

    
@app.route('/recommendations')
def recommendations():
   

    recc= sp.recommendations(seed_artists=[global_artist], seed_genres=[global_genre], seed_tracks=[global_track], limit= 5, country="US")
    recc_songs = {}
    for i in range(5):
        recc_songs[recc['tracks'][i]['name']] = recc['tracks'][i]['external_urls']['spotify']
        
    print(recc_songs)
    return render_template(
        'recommendations.html', 
        recc_songs=recc_songs,
        )

app.run(
    port = int(os.getenv("PORT", 8080)),
    host = os.getenv("IP", '0.0.0.0'),
    debug=True
)