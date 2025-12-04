# repository/hr_repository.py
from config.db import users_collection, tasks_collection

def get_all_users():
    return list(users_collection.find({}, {"password": 0}))

def get_all_tasks():
    return list(tasks_collection.find({}))
