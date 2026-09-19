import asyncio
from app.core.db import db

async def test():
    try:
        collections = await db.list_collection_names()
        print("✅ Connected successfully!")
        print("Collections in database:", collections)
    except Exception as e:
        print("❌ Connection failed:", e)

asyncio.run(test())