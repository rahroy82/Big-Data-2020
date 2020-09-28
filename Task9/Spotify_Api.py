
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time 
import pprint
import json
import requests
from kafka import KafkaProducer

bootstrap_servers = ['localhost:9099']
topicName = 'myTopic'


#Connect to the API
client_id = ' '
client_secret = ' '

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

 
getAll = sp.artist_albums('20qISvAhX20dpIbOOzGK3q',country='US',limit=50,)


dict_to_str = json.dumps(getAll)

pp = pprint.PrettyPrinter(depth=6)
pp.pprint(getAll)



writeFile =open('Spotify_artist_results_nas.txt', 'w')
writeFile.write(dict_to_str)
writeFile.close()



