import firebase_admin
from firebase_admin import credentials, firestore



# Set up Firestore
cred = credentials.Certificate('soft-eng-warmup-a838c198caa2.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

# Reference to your Firestore database
db = firestore.client()


# Function to populate the lowercase field
def create_lowercase_field():
    # Retrieve documents from the collection
    docs = db.collection("test-music").get()

    for doc in docs:
        # Get the value of YourField
        your_field_value = doc.get("`Artist Name`")
        # Create lowercase version of the value
        your_field_lower = your_field_value.lower()
        # Update the document with the lowercase value
        doc.reference.update({"`artist name`": your_field_lower})


# Call the function to populate the lowercase field
create_lowercase_field()

