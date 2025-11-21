
from pydantic import BaseModel
from typing import Optional

class TaskBase(BaseModel):
    title: str
    description: str
    status: str  

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None

class TaskResponse(TaskBase):
    id: str
    user_id: str  # intern id (owner)
    mentor_feedback: Optional[str] = None

    class Config:
        orm_mode = True
