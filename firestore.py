import firebase_admin
from firebase_admin import credentials, firestore
import json




# Delete old firestore
#Source: Firebase Documentation
def delete_collection(coll_ref, batch_size):
    docs = coll_ref.list_documents(page_size=batch_size)
    deleted = 0

    for doc in docs:
        print(f"Deleting doc {doc.id} => {doc.get().to_dict()}")
        doc.delete()
        deleted = deleted + 1

    if deleted >= batch_size:
        return delete_collection(coll_ref, batch_size)

def create_database(file_name):
    # Set up Firestore
    cred = credentials.Certificate('soft-eng-warmup-a838c198caa2.json')
    app = firebase_admin.initialize_app(cred)
    db = firestore.client()

    delete_collection(db.collection("test-music"), 35)

    # Open JSON File with explicit encoding
    with open('Music_Artists.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Add data to Firestore
    for artist in data['spotify_artists']:
        # Assuming 'test-music' is your collection name
        doc_ref = db.collection("test-music").document()
        doc_ref.set(artist)
        print(artist)

