from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Feedback(BaseModel):
    mentor_id: str
    comment: str
    date: datetime = datetime.utcnow()

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



