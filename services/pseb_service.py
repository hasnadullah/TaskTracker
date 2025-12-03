from config.db import users_collection, tasks_collection, Meetings_collection
from bson.objectid import ObjectId

def get_all_users():
    users = list(users_collection.find({}))
    for u in users:
        u["_id"] = str(u["_id"])
    return users

def get_all_tasks():
    tasks = list(tasks_collection.find({}))
    for t in tasks:
        t["_id"] = str(t["_id"])
    return tasks


def assign_task_to_mentor(task_id, mentor_id):
    tasks_collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": {"mentor_id": mentor_id}}
    )


def schedule_meeting(User_id: str, date: str, time: str , Note: str):
    Meetings_collection.insert_one({
        "user_id": ObjectId(User_id),
        "meeting_date": date,
        "meeting_time": time,
        "note": Note
    })
    

