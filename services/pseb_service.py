# services/pseb_service.py
from repository.pseb_repository import (
    find_all_users as repo_find_all_users,
    find_all_tasks as repo_find_all_tasks,
    assign_task,
    insert_meeting
)
from utils.id_converter import convert_object_ids

def get_all_users_service():
    users = repo_find_all_users()
    return convert_object_ids(users)

def get_all_tasks_service():
    tasks = repo_find_all_tasks()
    return convert_object_ids(tasks)

def assign_task_to_mentor_service(task_id, mentor_id):
    return assign_task(task_id, mentor_id)

def schedule_meeting_service(data: dict):
    return insert_meeting(data)
