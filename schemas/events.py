from pydantic import BaseModel
from datetime import datetime

class EventBase(BaseModel):
    title: str
    content: str

class EventCreate(EventBase):
    pass

class EventUpdate(EventBase):
    pass

class EventOut(EventBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
