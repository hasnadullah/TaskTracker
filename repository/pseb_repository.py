# repository/pseb_repository.py
from config.db import users_collection, tasks_collection, Meetings_collection
from bson.objectid import ObjectId

def find_all_users():
    return list(users_collection.find({}))

def find_all_tasks():
    return list(tasks_collection.find({}))

def assign_task(task_id: str, mentor_id: str):
    return tasks_collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": {"mentor_id": mentor_id}}
    )

def insert_meeting(data: dict):
    return Meetings_collection.insert_one(data)
