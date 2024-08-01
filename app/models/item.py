from pydantic import BaseModel
from typing import List

class DataItem(BaseModel):
    id: str
    valueType: str
    required: str
    regex: str
    value: str

class Item(BaseModel):
    trigger: str
    elementoId: str
    placeId: int
    data: List[DataItem]
