from services.pseb_service import (
    get_all_users,
    get_all_tasks,
    assign_task_to_mentor,
    schedule_meeting
)


def get_users_controller():
    return get_all_users()


def get_tasks_controller():
    return get_all_tasks()


def assign_task_controller(data):
    assign_task_to_mentor(data.task_id, data.mentor_id)
    return {"message": "Task assigned to mentor"}


def schedule_meeting_controller(data):
    schedule_meeting(data.User_id, data.date, data.time, data.Note)
    return {"message": "Meeting scheduled"}
