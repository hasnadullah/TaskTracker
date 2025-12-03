from fastapi import APIRouter, Depends
from controllers.meeting_controller import get_meetings_controller
from auth.jwt_bearer import JWTBearer

router = APIRouter(prefix="/meetings", tags=["meetings"])

@router.get("/")
def get_meetings(payload: dict = Depends(JWTBearer(["hr", "mentor", "pseb", "intern"]))):
    return get_meetings_controller()
