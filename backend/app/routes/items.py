from fastapi import APIRouter, HTTPException
from app.services.item_service import get_all_items

router = APIRouter()

@router.get("/items")
async def read_items():
    items = await get_all_items()
    if not items:
        raise HTTPException(status_code=404, detail="No items found")
    return items
