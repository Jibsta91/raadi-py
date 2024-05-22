from app.config import settings
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel

client = AsyncIOMotorClient(settings.MONGO_URI)
database = client[settings.DATABASE_NAME]
collection = database.get_collection("items")

class Item(BaseModel):
    name: str
    description: str

async def get_all_items():
    items = []
    async for item in collection.find():
        items.append(item)
    return items

async def create_item(item: Item):
    result = await collection.insert_one(item.dict())
    if result.inserted_id:
        return {**item.dict(), "id": str(result.inserted_id)}
    return None
