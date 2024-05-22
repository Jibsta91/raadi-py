from app.config import settings
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient(settings.MONGO_URI)
database = client[settings.DATABASE_NAME]
collection = database.get_collection("items")

async def get_all_items():
    items = []
    async for item in collection.find():
        items.append(item)
    return items
