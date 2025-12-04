# repository/user_repository.py
from config.db import users_collection
from bson.objectid import ObjectId

def insert_user(user_data):
    return users_collection.insert_one(user_data)

def find_user_by_email(email: str):
    return users_collection.find_one({"email": email})

def find_user_by_id(user_id: str):
    return users_collection.find_one({"_id": ObjectId(user_id)})

def find_all_users():
    return list(users_collection.find({}, {"password": 0}))
