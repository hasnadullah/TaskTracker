from fastapi import HTTPException
from services.pseb_service import (
    get_all_users_service,
    get_all_tasks_service,
    assign_task_to_mentor_service,
    schedule_meeting_service
)


def get_users_controller():
    try:
        return get_all_users_service()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def get_tasks_controller():
    try:
        return get_all_tasks_service()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def assign_task_controller(data):
    try:
        assign_task_to_mentor_service(data.task_id, data.mentor_id)
        return {"message": "Task assigned to mentor"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def schedule_meeting_controller(data: dict):
    try:
        schedule_meeting_service(data)
        return {"message": "Meeting scheduled"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
