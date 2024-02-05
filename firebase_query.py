import firebase_admin
from firebase_admin import credentials, firestore
import json

from google.cloud.firestore_v1 import FieldFilter

# Set up Firestore
cred = credentials.Certificate('soft-eng-warmup-a838c198caa2.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

music_ref = db.collection("test-music")

query = music_ref.where(filter=FieldFilter("Artist Name", "==", "Bad Bunny"))


queries = (
    music_ref
    .where(filter=FieldFilter("`Start Of Career`", "==", 2013))
    .stream()
)

for query in queries:
    print(f"{query.id} => {query.to_dict()}")