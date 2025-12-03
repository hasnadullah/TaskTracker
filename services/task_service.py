from repository.task_repository import (
    insert_task,
    find_tasks_by_intern,
    find_task_by_id,
    update_task,
    delete_task,
    add_feedback
)


def create_task(task_data):
    return insert_task(task_data)


def get_tasks_by_intern(intern_id):
    return find_tasks_by_intern(intern_id)


def get_task_by_id(task_id):
    return find_task_by_id(task_id)


def update_task_service(task_id, update_data):
    return update_task(task_id, update_data)


def delete_task_service(task_id):
    return delete_task(task_id)


def add_feedback_service(task_id, feedback):
    return add_feedback(task_id, feedback)
