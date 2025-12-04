# repository/task_repository.py
from config.db import tasks_collection
from bson.objectid import ObjectId
from datetime import datetime

def insert_task(task_data: dict):
    task_data.update({
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    })
    return tasks_collection.insert_one(task_data)

def find_tasks_by_intern(intern_id):
    return list(tasks_collection.find({"intern_id": intern_id}))

def find_task_by_id(task_id: str):
    return tasks_collection.find_one({"_id": ObjectId(task_id)})

def update_task(task_id: str, update_data: dict):
    update_data["updated_at"] = datetime.utcnow()
    return tasks_collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": update_data}
    )

def delete_task(task_id: str):
    return tasks_collection.delete_one({"_id": ObjectId(task_id)})

def add_feedback(task_id: str, feedback: dict):
    return tasks_collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$push": {"feedback": feedback}}
    )

def find_all_tasks():
    return list(tasks_collection.find({}))
