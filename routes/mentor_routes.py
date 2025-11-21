from fastapi import APIRouter, Depends
from controllers.mentor_controller import get_all_tasks_controller, add_feedback_controller
from auth.jwt_bearer import JWTBearer

router = APIRouter(prefix="/mentor", tags=["mentor"])

@router.get("/tasks")
def all_tasks(payload: dict = Depends(JWTBearer(["mentor"]))):
    return get_all_tasks_controller()

@router.post("/tasks/{task_id}/feedback")
def add_feedback(task_id: str, comment: str, payload: dict = Depends(JWTBearer(["mentor"]))):
    return add_feedback_controller(task_id, comment, payload["user_id"])
