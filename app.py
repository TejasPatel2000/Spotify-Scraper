# Import all necessary packages/libraries
from flask import Flask, render_template, request
import random
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv, find_dotenv

# Load env variables from .env file that is hidden
load_dotenv(find_dotenv())

# Creates Flask Instance
app = Flask(__name__)

# Authorizes Spotify Credentials that are set locally using SpotifyClientCredentials Method
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# Intialize global variables as it will be needed to find recommended songs
global_artist = ""
global_track = ""
global_track_name= ""
global_genre = ""

# Create default homepage
@app.route('/')
def hello_world():
    # hard code ids of 3 artists
    fav_artists_id   = ["6l3HvQ5sa6mXTsMTB19rO5", "55Aa2cqylxrFIXC767Z865", "3TVXtAsR1Inumwj472S9r4"]
    # Use random num to choose artist and begin parsing data from them using spotipy methods 
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
    
    # Set global vars here so that this info will be accessible in recommendations method.
    # Need to do this inside method otherwise it won't update each time you refresh the page
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
    # Get 5 reccomended songs based off artist, current track, and genre in US
    recc= sp.recommendations(seed_artists=[global_artist], seed_genres=[global_genre], seed_tracks=[global_track], limit= 5, country="US")
    recc_songs = {}
    # For loop to iterate over each track and link the name of the song to its url to play
    for i in range(5):
        recc_songs[recc['tracks'][i]['name']] = recc['tracks'][i]['external_urls']['spotify']
        
    return render_template(
        'recommendations.html', 
        recc_songs=recc_songs,
        global_track_name = global_track_name,
        )
        

@app.route('/findArtist', methods = ['POST', 'GET'])
def findArtist():
    # Use of POST method and forms to add functionality to search for aritsts
    if request.method == 'POST':
        data = request.form['artist_search']
        # Check if user left text box empty
        if data != "":
            temp = sp.search(q=data, type="artist", limit=1)
            # Check to make sure artist exists. If not --> return error page
            if (len(temp['artists']['items']))==0:
                return render_template(
                'error.html',
                data=data,
                )
            else:
                # Get first artist based off search
                artist = temp['artists']['items'][0]["id"]
        
                name = sp.artist(artist)['name']
     
                random_number = random.randint(0,9)
                # Ensure they are an artist with tracks and are classified with a genre
                if  len(sp.artist_top_tracks(artist, "US")['tracks']) >= 9 and len(sp.artist(artist)['genres']) > 0:
                    track_name = sp.artist_top_tracks(artist, "US")['tracks'][random_number]["name"]
                    track_href=sp.artist_top_tracks(artist, "US")['tracks'][random_number]['external_urls']['spotify']
                    track_id = sp.artist_top_tracks(artist, "US")['tracks'][random_number]['id']
                    
                    artist_pic = sp.artist(artist)["images"][2]['url']
                    
                    prev_url = sp.artist_top_tracks(artist, "US")['tracks'][random_number]["preview_url"]
                    img_url = sp.artist_top_tracks(artist,"US")["tracks"][random_number]["album"]["images"][0]["url"]
                    
                    genre = sp.artist(artist)['genres'][0]
                    
                     # Set global vars here so that this info will be accessible in recommendations method.
                     # Need to do this inside method otherwise it won't update each time you refresh the page
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
        else:
            return render_template(
                'error.html',
                data = data)
    
# Run Flask Application
app.run(
    port = int(os.getenv("PORT", 8080)),
    host = os.getenv("IP", '0.0.0.0'),
    debug=True
)