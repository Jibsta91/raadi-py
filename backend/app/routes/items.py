from fastapi import APIRouter, HTTPException, Body
from app.services.item_service import create_item
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str

router = APIRouter()

@router.get("/items")
async def read_items():
    return await get_all_items()

@router.post("/items")
async def add_item(item: Item = Body(...)):
    created_item = await create_item(item)
    if created_item:
        return created_item
    raise HTTPException(status_code=400, detail="Item creation failed")
