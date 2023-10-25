import spotipy
from spotipy.oauth2 import SpotifyOAuth
from skpy import Skype, SkypeAuthException
from time import sleep  # Import sleep function for delay

# Set up Spotify API authentication
scope = 'user-read-currently-playing'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope=scope,
    client_id='INSERT SPOTIFY CLIENT ID HERE',
    client_secret='CLIENT SECRET',
    redirect_uri='http://localhost:8080/callback'
))

# Check if a song is currently playing
def get_current_song_info():
    result = sp.currently_playing()
    if result is not None and 'item' in result:
        song_name = result['item']['name']
        artist_name = result['item']['artists'][0]['name']
        return song_name, artist_name
    else:
        return None, None

# Initialize Skype mood updater
sk = Skype()
try:
    sk.conn.liveLogin("SKYPE ACCOUNT EMAIL", "SKYPE ACCOUNT PASSWORD")
    print("Success: Logged in to Skype.")
except SkypeAuthException:
    print("Error: Failed to log in to Skype.")

# Declare mood_text outside of mood_updater
mood_text = "1"
previous_song = None  # Variable to store previous song

# Mood Updater
def mood_updater(current_song, artist_name):
    global mood_text, previous_song  # Use the global mood_text and previous_song variables
    if current_song is not None and current_song != previous_song:
        mood_text = f"(speakermedium) Listening To: {current_song} - {artist_name}"
        previous_song = current_song  # Update previous_song with the current_song
    sk.setMood(mood_text)

while True:
    current_song, artist_name = get_current_song_info()
    if current_song is not None and current_song != previous_song:
        print(f"Listening to: {current_song} - {artist_name}")
        mood_updater(current_song, artist_name)
    else:
        print("Same song is playing!")
    sleep(15)  # Delay for 15 seconds before checking again
