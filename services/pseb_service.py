from repository.pseb_repository import (
    find_all_users,
    find_all_tasks,
    assign_task,
    insert_meeting
)


def get_all_users():
    return find_all_users()


def get_all_tasks():
    return find_all_tasks()


def assign_task_to_mentor(task_id, mentor_id):
    return assign_task(task_id, mentor_id)


def schedule_meeting(user_id, date, time, note):
    return insert_meeting(user_id, date, time, note)
