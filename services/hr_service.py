# services/hr_service.py
from repository.hr_repository import get_all_users as repo_get_all_users, get_all_tasks as repo_get_all_tasks
from utils.id_converter import convert_object_ids

def get_all_users_service():
    users = repo_get_all_users()
    return convert_object_ids(users)

def get_all_tasks_service():
    tasks = repo_get_all_tasks()
    return convert_object_ids(tasks)
