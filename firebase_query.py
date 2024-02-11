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
generic_array = [["artist name", "location"], [["start of career", "==", 2006]]]
#generic_array = ["Artist Name", [["Location", "==", "Canada"], ["Name", "==", "Drake"]]]

#compound_generic_array = ["Artist Name", "Location"]
song_array = ["Artist Name", [["Songs", "==", "Beat it"]]]
genre_array = ["Artist Name", [["Genre", "==", "Pop"]]]


# function for user data
def querying_user_data(user_data):
    # if statement for second element, which would have either song or genre. Here, we'll have contains
    # as a conditional to select all records which contain some of the user input, such as an incomplete song or genre

    #user_data = [i.lower() for i in user_data[1:]]
    for conditions in user_data[1]:
        queries = ""

        if queries:
            if conditions[0] == "Songs" or conditions[0] == "Genre":
                if conditions[1] == "==":
                    queries = queries.where(filter=FieldFilter("`" + conditions[0] + "`", "array_contains_any", [conditions[2]]))
                else:
                    queries = queries.where(filter=FieldFilter("`" + conditions[0] + "`", "not in", [conditions[2]]))
            else:
                queries = queries.where(filter=FieldFilter("`" + conditions[0] + "`", conditions[1], conditions[2]))
        else:
            if conditions[0] == "Songs" or conditions[0] == "Genre":
                if conditions[1] == "==":
                    queries = (music_ref
                           .where(filter=FieldFilter("`" + conditions[0] + "`", "array_contains_any", [conditions[2]])))
                else:
                    queries = queries.where(filter=FieldFilter("`" + conditions[0] + "`", "not in", [conditions[2]]))
            else:
                queries = (
                    music_ref
                    .where(filter=FieldFilter("`" + conditions[0] + "`", conditions[1], conditions[2]))
                )
        #print(queries)

    queries = queries.stream()
    for query in queries:
        query_dict = query.to_dict()
        #print(query_dict)
        if user_data[0] == 'all':
            print(query_dict)
        else:
            print(query_dict[user_data[0]])






querying_user_data(generic_array)
