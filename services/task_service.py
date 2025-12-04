# services/task_service.py
from repository.task_repository import (
    insert_task,
    find_tasks_by_intern,
    find_task_by_id,
    update_task,
    delete_task,
    add_feedback,
    find_all_tasks as repo_find_all_tasks
)
from utils.id_converter import convert_object_ids

def create_task_service(task_data):
    result = insert_task(task_data)
    task = dict(task_data)
    task["_id"] = str(result.inserted_id)
    return convert_object_ids(task)

def get_tasks_by_intern_service(intern_id):
    tasks = find_tasks_by_intern(intern_id)
    return convert_object_ids(tasks)

def get_task_by_id_service(task_id):
    task = find_task_by_id(task_id)
    return convert_object_ids(task)

def update_task_service(task_id, update_data):
    update_task(task_id, update_data)
    updated = find_task_by_id(task_id)
    return convert_object_ids(updated)

def delete_task_service(task_id):
    return delete_task(task_id)

def add_feedback_service(task_id, feedback):
    return add_feedback(task_id, feedback)

def get_all_tasks_service():
    tasks = repo_find_all_tasks()
    return convert_object_ids(tasks)
