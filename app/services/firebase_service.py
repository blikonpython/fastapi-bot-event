from app.core.config import firebase_config
from app.models.item import Item

class FirebaseService:
    def __init__(self):
        self.db = firebase_config.db

    def save_item(self, item: Item):
        try:
            doc_ref = self.db.collection('items').document(item.elementoId)
            doc_ref.set(item.dict())
            return {"message": "Data saved successfully"}
        except Exception as e:
            return {"error": str(e)}

firebase_service = FirebaseService()
