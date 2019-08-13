#!/usr/bin/env python

import spotipy
import os

from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint

# Start here:
# https://spotipy.readthedocs.io/en/latest/

# Register your app here and get your client ID and secret:
# https://developer.spotify.com/dashboard/applications

# Then, modify with this, and it works:
# https://github.com/plamere/spotipy/issues/194#issuecomment-315458391

client_id     = os.environ['SPOTIFY_CLIENT_ID']
client_secret = os.environ['SPOTIFY_CLIENT_SECRET']

print(client_id)
print(client_secret)

client_credentials_manager = SpotifyClientCredentials(client_id=client_id,
                                                      client_secret=client_secret)
name = "beyonce"

spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
results = spotify.search(q='artist:' + name, type='artist')
pprint(results)
