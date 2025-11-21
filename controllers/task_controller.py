from fastapi import HTTPException
from services.task_service import create_task, get_tasks_by_intern, get_task_by_id, update_task, delete_task
from datetime import datetime

def create_task_controller(task_data, intern_id):
    task_dict = task_data.dict()
    task_dict.update({"intern_id": intern_id, "status": "pending", "feedback": []})
    result = create_task(task_dict)
    return {"message": "Task created", "task_id": str(result.inserted_id)}

def get_my_tasks_controller(intern_id):
    return get_tasks_by_intern(intern_id)

def update_task_controller(task_id, task_data, intern_id):
    task = get_task_by_id(task_id)
    if not task or task["intern_id"] != intern_id:
        raise HTTPException(status_code=404, detail="Task not found")
    update_task(task_id, task_data.dict(exclude_unset=True))
    return {"message": "Task updated"}

def delete_task_controller(task_id, intern_id):
    task = get_task_by_id(task_id)
    if not task or task["intern_id"] != intern_id:
        raise HTTPException(status_code=404, detail="Task not found")
    delete_task(task_id)
    return {"message": "Task deleted"}
