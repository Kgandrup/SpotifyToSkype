# SpotifyToSkype
A simple program to take a user's currently listening and display is as your Skype Mood/Status message

Roadmap:
Ability to see song progress in the status
Lyrics command?

Also I know the code sucks. I haven't coded in python in like 3-4 years... And there are still a lot of issues I'm uncovering with the current functionality. I'll probably work on the code here and there. This was more like a 'for fun' project than something to try and market and publish.



Required Dependencies:
--------------
Python 3.11 or later

Spotipy

SkPy

time

# Setup:

Download the folder and open in any code editing program. Open the spotifytoskype.py file and look for a couple of blank spaces.

Firstly, you need to have an active spotify account. Go to the spotify developers website (https://developer.spotify.com/dashboard). Click "Create app", give it any name and description you would like.  Make sure to set the Redirect URL to http://localhost:8080/callback

After you create the app on the developer site, copy the client ID and client secret into their respective locations. 

Next, you need to log into your Skype account so it can update the status properly. Input the email and password for your skype/microsoft account linked with the Skype account you want to use in the two slots on line 28 (sk.conn.livelogin("Email", "Password").

The program should be ready to run!



# Customization:

If you want to customize the messages, you can edit them on line 41. Line 41 is the actual status message. You can edit anything in there except the {current_song} and {artist_name} variables.
If no song is playing, you can set the mood message to a specific message on line 34. If you leave it blank, your status will go blank.

If you want the program to check for song statuses faster, update line 56's "sleep" command to a lower number. 



## NOTE: 
Skype does take time to update the status server side. There is nothing that can be done to avoid that. Spotify also takes 5-10 minutes to detect that no song is playing, due to how the API works. I wish there was a way to lower that timing down but as of right now its unavoidable
