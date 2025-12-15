from pymongo import MongoClient

print("🔄 Starting MongoDB connection test...")

try:
    client = MongoClient("mongodb://localhost:27017", serverSelectionTimeoutMS=3000) # we have to change the local host path of this from here and keep it as

    # Force connection
    client.admin.command("ping")

    print("✅ MongoDB connected successfully!")

    db = client["langgraph_db"]
    collection = db["test_collection"]

    result = collection.insert_one({"msg": "Hello from Python"})
    print("✅ Test document inserted with ID:", result.inserted_id)

except Exception as e:
    print("❌ MongoDB connection failed")
    print(e)
