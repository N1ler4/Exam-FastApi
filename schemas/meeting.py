from pydantic import BaseModel
from datetime import datetime

class MeetingBase(BaseModel):
    title: str
    content: str

class MeetingCreate(MeetingBase):
    pass

class MeetingUpdate(MeetingBase):
    pass

class MeetingOut(MeetingBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
