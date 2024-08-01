from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.models.item import Item
from app.services.firebase_service import firebase_service
import json
import os

router = APIRouter()

# Ruta a la carpeta de datos
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')


@router.get("/items/mexicanna.json")
async def get_mexicanna():
    file_path = os.path.join(DATA_DIR, 'mexicanna.json')
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    with open(file_path, 'r') as file:
        data = json.load(file)

    return JSONResponse(content=data)


@router.post("/items", response_model=dict)
async def create_item(item: Item):
    response = firebase_service.save_item(item)
    if "error" in response:
        error_file_path = os.path.join(DATA_DIR, 'error.json')
        with open(error_file_path, 'r') as file:
            error_data = json.load(file)
        raise HTTPException(status_code=400, detail=error_data)

    message_file_path = os.path.join(DATA_DIR, 'mensaje.json')
    with open(message_file_path, 'r') as file:
        message_data = json.load(file)

    return JSONResponse(content=message_data)
