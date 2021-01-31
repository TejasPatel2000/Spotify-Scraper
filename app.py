from flask import Flask, render_template
import random
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


app = Flask(__name__)

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


@app.route('/')
def hello_world():
    fav_artists_name = ["J Cole", "Lil Wayne", "Drake"]
    fav_artists_id   = ["6l3HvQ5sa6mXTsMTB19rO5", "55Aa2cqylxrFIXC767Z865", "3TVXtAsR1Inumwj472S9r4"]
    random_number = random.randint(0,2)
    artist = fav_artists_id[random_number]
    
    random_number = random.randint(0,9)
    name = sp.artist(artist)['name']
    track_name = sp.artist_top_tracks(artist, "US")['tracks'][random_number]["name"]
    prev_url = sp.artist_top_tracks(artist, "US")['tracks'][random_number]["preview_url"]
    img_url = sp.artist_top_tracks(artist,"US")["tracks"][random_number]["album"]["images"][0]["url"]
    print(name)
    print(track_name)
    print(prev_url)
    print(img_url)
    return render_template(
        'index.html', 
        name = name,
        track = track_name,
        prev_url = prev_url,
        image=img_url,
        )

    

app.run(
    port = int(os.getenv("PORT", 8080)),
    host = os.getenv("IP", '0.0.0.0'),
    debug=True
)