from config.db import users_collection, tasks_collection, Meetings_collection
from bson.objectid import ObjectId


def find_all_users():
    users = list(users_collection.find({}))
    for u in users:
        u["_id"] = str(u["_id"])
    return users


def find_all_tasks():
    tasks = list(tasks_collection.find({}))
    for t in tasks:
        t["_id"] = str(t["_id"])
    return tasks


def assign_task(task_id: str, mentor_id: str):
    tasks_collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": {"mentor_id": mentor_id}}
    )


def insert_meeting(user_id: str, date: str, time: str, note: str):
    Meetings_collection.insert_one({
        "user_id": ObjectId(user_id),
        "meeting_date": date,
        "meeting_time": time,
        "note": note
    })
