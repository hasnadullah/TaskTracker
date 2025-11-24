from fastapi import APIRouter, Depends
from controllers.hr_controller import get_all_users_controller, get_all_tasks_controller
from auth.jwt_bearer import JWTBearer

router = APIRouter(prefix="/hr", tags=["hr"])


@router.get("/users")
def all_users(payload: dict = Depends(JWTBearer(["hr"]))):
    return get_all_users_controller()


@router.get("/tasks")
def all_tasks(payload: dict = Depends(JWTBearer(["hr"]))):
    return get_all_tasks_controller()
