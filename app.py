from flask import Flask, render_template, request
import random
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

app = Flask(__name__)

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


global_artist = ""
global_track = ""
global_track_name= ""
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
    
    artist_pic = sp.artist(artist)["images"][2]['url']
    
    prev_url = sp.artist_top_tracks(artist, "US")['tracks'][random_number]["preview_url"]
    img_url = sp.artist_top_tracks(artist,"US")["tracks"][random_number]["album"]["images"][0]["url"]
    
    genre = sp.artist(artist)['genres'][0]
    
    global global_artist
    global_artist = artist
    
    global global_track
    global_track = track_id
    
    global global_track_name
    global_track_name = track_name
    global global_genre
    global_genre = genre
    
    # Use Genius API to find lyrics 
    genius_base_url = "http://api.genius.com"
    headers = {'Authorization': 'Bearer ' + os.getenv('GENIUS_ACCESS_TOKEN')}
    search_url = genius_base_url + '/search'
    data = {'q':track_name+ ' ' + name }
    response= requests.get(search_url, params=data, headers=headers)
    json = response.json()
    lyrics_url = json['response']['hits'][0]['result']['url']
    
    return render_template(
        'index.html', 
        name = name,
        track = track_name,
        prev_url = prev_url,
        image=img_url,
        track_href = track_href,
        artist_pic = artist_pic,
        lyrics_url = lyrics_url,
        )

    
@app.route('/recommendations')
def recommendations():
    recc= sp.recommendations(seed_artists=[global_artist], seed_genres=[global_genre], seed_tracks=[global_track], limit= 5, country="US")
    recc_songs = {}
    for i in range(5):
        recc_songs[recc['tracks'][i]['name']] = recc['tracks'][i]['external_urls']['spotify']
        
    return render_template(
        'recommendations.html', 
        recc_songs=recc_songs,
        global_track_name = global_track_name,
        )
        

@app.route('/findArtist', methods = ['POST', 'GET'])
def findArtist():
    if request.method == 'POST':
        data = request.form['artist_search']

        temp = sp.search(q=data, type="artist", limit=1)

        if (len(temp['artists']['items']))==0:
            return render_template(
            'error.html',
            data=data,
            )
        else:
            artist = temp['artists']['items'][0]["id"]
    
            name = sp.artist(artist)['name']
 
            random_number = random.randint(0,9)
            if  len(sp.artist_top_tracks(artist, "US")['tracks']) >= 9 and len(sp.artist(artist)['genres']) > 0:
                track_name = sp.artist_top_tracks(artist, "US")['tracks'][random_number]["name"]
                track_href=sp.artist_top_tracks(artist, "US")['tracks'][random_number]['external_urls']['spotify']
                track_id = sp.artist_top_tracks(artist, "US")['tracks'][random_number]['id']
                
                artist_pic = sp.artist(artist)["images"][2]['url']
                
                prev_url = sp.artist_top_tracks(artist, "US")['tracks'][random_number]["preview_url"]
                img_url = sp.artist_top_tracks(artist,"US")["tracks"][random_number]["album"]["images"][0]["url"]
                
                genre = sp.artist(artist)['genres'][0]
                
                global global_artist
                global_artist = artist
            
                global global_track
                global_track = track_id
                
                global global_track_name
                global_track_name = track_name
            
                global global_genre
                global_genre = genre
                
                # Use Genius API to find lyrics 
                genius_base_url = "http://api.genius.com"
                headers = {'Authorization': 'Bearer ' + os.getenv('GENIUS_ACCESS_TOKEN')}
                search_url = genius_base_url + '/search'
                search_data = {'q':track_name+ ' ' + name }
                response= requests.get(search_url, params=search_data, headers=headers)
                json = response.json()
                if len(json['response']['hits']) > 0:
                    lyrics_url = json['response']['hits'][0]['result']['url']
                        
                    return render_template(
                        'findArtist.html',
                        name = name,
                        track = track_name,
                        prev_url = prev_url,
                        image=img_url,
                        track_href = track_href,
                        artist_pic = artist_pic,
                        lyrics_url = lyrics_url,
                        )
                else:
                    return render_template(
                        'error.html',
                        data=data,
                    )
            else:
                return render_template(
                    'error.html',
                    data=data,
                    )
    

app.run(
    port = int(os.getenv("PORT", 8080)),
    host = os.getenv("IP", '0.0.0.0'),
    debug=True
)