from fastapi import APIRouter, Depends
from schemas.task_schema import TaskCreate, TaskUpdate
from controllers.task_controller import create_task_controller, get_my_tasks_controller, update_task_controller, delete_task_controller
from auth.jwt_bearer import JWTBearer

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/create")
def create_task(task: TaskCreate, payload: dict = Depends(JWTBearer(["intern"]))):
    return create_task_controller(task, payload["user_id"])

@router.get("/my")
def get_my_tasks(payload: dict = Depends(JWTBearer(["intern"]))):
    return get_my_tasks_controller(payload["user_id"])

@router.put("/update/{task_id}")
def update_task(task_id: str, task: TaskUpdate, payload: dict = Depends(JWTBearer(["intern"]))):
    return update_task_controller(task_id, task, payload["user_id"])

@router.delete("/delete/{task_id}")
def delete_task(task_id: str, payload: dict = Depends(JWTBearer(["intern"]))):
    return delete_task_controller(task_id, payload["user_id"])
