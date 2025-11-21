from fastapi import APIRouter, Depends
from models.user_model import UserCreate, UserLogin
from controllers.user_controller import signup_controller, login_controller
from auth.jwt_bearer import JWTBearer

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup")
def signup(user: UserCreate):
    return signup_controller(user)

@router.post("/login")
def login(user: UserLogin):
    return login_controller(user)

@router.get("/me")
def get_me(payload: dict = Depends(JWTBearer())):
    return payload
