from fastapi import HTTPException
from services.user_service import create_user, get_user_by_email
from auth.jwt_handler import create_access_token


def signup_controller(user_data):
    result = create_user(user_data.dict())
    if not result:
        raise HTTPException(status_code=400, detail="Email already exists")
    return {"message": "User created successfully"}


def login_controller(user_data):
    db_user = get_user_by_email(user_data.email)
    if not db_user or db_user["password"] != user_data.password:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_access_token({
        "user_id": str(db_user["_id"]),
        "role": db_user["role"]
    })

    return {"token": token}
