from config.db import users_collection, tasks_collection
from bson.objectid import ObjectId

def get_all_users_controller():
    users = list(users_collection.find({}, {"password": 0}))  # exclude password
    for u in users:
        u["_id"] = str(u["_id"])
    return users

def get_all_tasks_controller():
    tasks = list(tasks_collection.find({}))
    for t in tasks:
        t["_id"] = str(t["_id"])
    return tasks