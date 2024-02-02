import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

#Set up Firestore
cred = credentials.Certificate('soft-eng-warmup-a838c198caa2.json')

app = firebase_admin.initialize_app(cred)
db = firestore.client()

#Open JSON File
f = open('Music_Artists.json')
data = json.load(f)

# add_data
for artist in data['spotify_artists']:
    # doc_ref = db.collection("test-music").document()
    # doc_ref.set(artist)
    print(artist)