# Import necessary libraries
import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1 import FieldFilter

# Initialize Firebase Admin SDK

# Function to query user data from Firestore
def querying_user_data(user_data):
    """
    Function to query user data from Firestore based on given conditions.

    Args:
        user_data (list): A list containing user query data.

    Returns:
        None
    """

    # Set up Firestore
    db = firestore.client()
    music_ref = db.collection("test-music")

    queries = ""  # Initialize queries variable

    # Check if user_data contains more than one condition
    if len(user_data) > 1:
        for conditions in user_data[1:]:
            # Construct query based on conditions
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

    else:
        queries = music_ref  # If only one condition, set queries to reference the entire collection

    # Execute queries and process results
    queries = queries.stream()
    list_info = []
    for query in queries:
        query_dict = query.to_dict()
        if user_data[0] == 'all':
            # Print all information for each document
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
                # Handle specific field data retrieval
                data = ""
                for word in query_dict[user_data[0]].split(" "):
                    data += f"{word.capitalize()}"
                list_info.append(data)
            except AttributeError:
                for info in query_dict[user_data[0]]:
                    list_info.append(info.capitalize())

    if user_data[0] != 'all':
        # Display results for specific field
        list_info = list(set(list_info))
        print(f"{user_data[0].capitalize()}s: {list_info}")

# Entry point of the program
if __name__ == "__main__":
    # Example usage of querying_user_data function
    # Define user data
    # For example: ['all', ['artist name', '==', 'Drake']]
    user_data = ['all', ['artist name', '==', 'Drake']]

    # Call querying_user_data function with user data
    querying_user_data(user_data)