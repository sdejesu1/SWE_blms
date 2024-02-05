import firebase_admin
from firebase_admin import credentials, firestore
import json

# Set up Firestore
cred = credentials.Certificate('soft-eng-warmup-a838c198caa2.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

# Open JSON File with explicit encoding
with open('Music_Artists.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Add data to Firestore
for artist in data['spotify_artists']:
    # Assuming 'test-music' is your collection name
    doc_ref = db.collection("test-music").document()
    doc_ref.set(artist)
    print(artist)
