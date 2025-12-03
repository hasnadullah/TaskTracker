from config.db import users_collection, tasks_collection


def get_all_users():
    users = list(users_collection.find({}, {"password": 0}))
    for u in users:
        u["_id"] = str(u["_id"])
    return users


def get_all_tasks():
    tasks = list(tasks_collection.find({}))
    for t in tasks:
        t["_id"] = str(t["_id"])
    return tasks
