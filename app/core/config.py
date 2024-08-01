import os
import json
import firebase_admin
from firebase_admin import credentials, firestore

class FirebaseConfig:
    def __init__(self):
        cred_info = os.getenv("FIREBASE_CREDENTIALS")
        if cred_info:
            cred = credentials.Certificate(json.loads(cred_info))
            firebase_admin.initialize_app(cred)
            self.db = firestore.client()

firebase_config = FirebaseConfig()
