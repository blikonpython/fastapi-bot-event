import firebase_admin
from firebase_admin import credentials, firestore

class FirebaseConfig:
    def __init__(self):
        cred = credentials.Certificate("app/firebase_credentials.json")
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()

firebase_config = FirebaseConfig()
