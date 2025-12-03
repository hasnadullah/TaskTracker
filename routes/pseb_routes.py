from fastapi import APIRouter, Depends
from controllers.pseb_controller import (
    get_users_controller,
    get_tasks_controller,
    assign_task_controller,
    schedule_meeting_controller
)
from auth.jwt_bearer import JWTBearer
from schemas.task_schema import AssignTaskSchema
from schemas.task_schema import ScheduleMeetingSchema

router = APIRouter(prefix="/pseb", tags=["pseb"])

@router.get("/users")
def get_users(payload: dict = Depends(JWTBearer(["pseb"]))):
    return get_users_controller()

@router.get("/tasks")
def get_tasks(payload: dict = Depends(JWTBearer(["pseb"]))):
    return get_tasks_controller()

@router.post("/assign-task")
def assign_task(data: AssignTaskSchema, payload: dict = Depends(JWTBearer(["pseb"]))):
    return assign_task_controller(data)

@router.post("/schedule-meeting")
def schedule_meeting(data: ScheduleMeetingSchema, payload: dict = Depends(JWTBearer(["pseb"]))):
    return schedule_meeting_controller(data)
