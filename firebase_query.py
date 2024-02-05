import firebase_admin
from firebase_admin import credentials, firestore
import json

from google.cloud.firestore_v1 import FieldFilter

# Set up Firestore
cred = credentials.Certificate('soft-eng-warmup-a838c198caa2.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

music_ref = db.collection("test-music")

# test arrays - remaining test arrays: compound queries (AND)
generic_array = ["Artist Name", "Location", "==", "Canada"]
song_array = ["Artist Name", "Songs", "==", "Beat it"]
genre_array = ["Artist Name", "Genre", "==", "Pop"]


# function for user data
def querying_user_data(user_data):
    # if statement for second element, which would have either song or genre. Here, we'll have contains
    # as a conditional to select all records which contain some of the user input, such as an incomplete song or genre
    if user_data[1] == "Songs" or user_data[1] == "Genre":
        queries = (
            music_ref
            .where(filter=FieldFilter("`" + user_data[1] + "`", "array_contains_any", [user_data[3]]))
            .stream()
        )
        for query in queries:
            query_dict = query.to_dict()
            print(query_dict[user_data[0]])

    else:
        queries = (
            music_ref
            .where(filter=FieldFilter("`" + user_data[1] + "`", user_data[2], user_data[3]))
            .stream()
        )

        for query in queries:
            query_dict = query.to_dict()
            print(query_dict[user_data[0]])


querying_user_data(song_array)
