from config.db import tasks_collection
from bson.objectid import ObjectId
from datetime import datetime

def create_task(task_data):
    task_data.update({"created_at": datetime.utcnow(), "updated_at": datetime.utcnow()})
    return tasks_collection.insert_one(task_data)

def get_tasks_by_intern(intern_id):
    tasks = list(tasks_collection.find({"intern_id": intern_id}))
    for t in tasks:
        t["_id"] = str(t["_id"])
    return tasks

def get_task_by_id(task_id):
    return tasks_collection.find_one({"_id": ObjectId(task_id)})

def update_task(task_id, update_data):
    update_data["updated_at"] = datetime.utcnow()
    tasks_collection.update_one({"_id": ObjectId(task_id)}, {"$set": update_data})

def delete_task(task_id):
    tasks_collection.delete_one({"_id": ObjectId(task_id)})

def add_feedback(task_id, feedback):
    tasks_collection.update_one({"_id": ObjectId(task_id)}, {"$push": {"feedback": feedback}})
