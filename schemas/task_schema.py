
from pydantic import BaseModel
from typing import Optional
from typing import List, Optional
from datetime import datetime

class AssignTaskSchema(BaseModel):
    task_id: str
    mentor_id: str

class ScheduleMeetingSchema(BaseModel):
    User_id: str
    date: str
    time: str
    Note: str

class Feedback(BaseModel):
    mentor_id: str
    comment: str

class TaskCreate(BaseModel):
    title: str
    description: str

class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[str]

class Task(TaskCreate):
    intern_id: str
    status: str = "pending"
    feedback: List[Feedback] = []
    meeting_date: Optional[str] = None
    meeting_time: Optional[str] = None
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()

class AssignTaskModel(BaseModel):
    task_id: str
    mentor_id: str

class ScheduleMeetingModel(BaseModel):
    task_id: str
    date: str
    time: str
