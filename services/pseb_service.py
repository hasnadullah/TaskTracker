from config.db import users_collection, tasks_collection
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

def schedule_meeting(task_id, date, time):
    tasks_collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": {"meeting_date": date, "meeting_time": time}}
    )
