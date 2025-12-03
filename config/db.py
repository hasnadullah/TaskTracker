from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["internship_tracker"]

users_collection = db["users"]
tasks_collection = db["tasks"]
Meetings_collection = db["Mettings"]
