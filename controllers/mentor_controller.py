from fastapi import HTTPException
from services.task_service import get_task_by_id, add_feedback_service
from datetime import datetime


def get_all_tasks_controller():
    from repository.task_repository import find_all_tasks
    return find_all_tasks()


def add_feedback_controller(task_id, comment, mentor_id):
    task = get_task_by_id(task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    feedback = {
        "mentor_id": mentor_id,
        "comment": comment,
        "date": datetime.utcnow()
    }

    add_feedback_service(task_id, feedback)
    return {"message": "Feedback added"}
