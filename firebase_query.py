import firebase_admin
from firebase_admin import credentials, firestore
import json

from google.cloud.firestore_v1 import FieldFilter



# # test arrays - remaining test arrays: compound queries (AND)
#generic_array = ["all", [["start of career", "==", 2006]]]
generic_array = ["artist name", [["location", "==", "canada"], ["genre", "==", "hip hop/rap"]]]
#
# #compound_generic_array = ["Artist Name", "Location"]
# song_array = ["Artist Name", [["Songs", "==", "Beat it"]]]
#genre_array = ["artist name", [["genre", "==", "pop"]]]


# function for user data
def querying_user_data(user_data):
    # Set up Firestore
    cred = credentials.Certificate('soft-eng-warmup-a838c198caa2.json')
    app = firebase_admin.initialize_app(cred)
    db = firestore.client()

    music_ref = db.collection("test-music")

    # if statement for second element, which would have either song or genre. Here, we'll have contains
    # as a conditional to select all records which contain some of the user input, such as an incomplete song or genre

    queries = ""
    #user_data = [i.lower() for i in user_data[1:]]
    for conditions in user_data[1]:

        if queries:
            if conditions[0] == "songs" or conditions[0] == "genre":
                if conditions[1] == "==":
                    queries = queries.where(filter=FieldFilter("`" + conditions[0] + "`", "array_contains_any", [conditions[2]]))
                else:
                    queries = queries.where(filter=FieldFilter("`" + conditions[0] + "`", "not in", [conditions[2]]))
            else:
                queries = queries.where(filter=FieldFilter("`" + conditions[0] + "`", conditions[1], conditions[2]))
        else:
            if conditions[0] == "songs" or conditions[0] == "genre":
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
    list_info = []
    for query in queries:
        query_dict = query.to_dict()
        #print(query_dict)
        if user_data[0] == 'all':
            for key in query_dict:
                if key != "end of career" and key != "start of career":
                    if isinstance(query_dict[key], str):
                        print(key.capitalize() + ": " + query_dict[key].title())
                    elif isinstance(query_dict[key], list):
                        capitalized_list = [word.title() for word in query_dict[key]]
                        print(key.capitalize() + ": " + str(capitalized_list))
                    else:
                        print(key.capitalize() + ": " + str(query_dict[key]))
                elif key == "end of career" or key == "start of career":
                    print(key.capitalize() + ": " + str(query_dict[key]))
            print("\n")
        else:
            try:
                data = ""
                for word in query_dict[user_data[0]].split(" "):
                    data += f"{word.capitalize()}"
                list_info.append(data)
            except AttributeError:
                for info in query_dict[user_data[0]]:
                    list_info.append(info.capitalize())

    if user_data[0] != 'all':
        list_info = list(set(list_info))
        print(f"{user_data[0].capitalize()}s: {list_info}")


querying_user_data(generic_array)

