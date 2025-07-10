from pydantic import BaseModel
from datetime import datetime

class SeminarBase(BaseModel):
    title: str
    content: str

class SeminarCreate(SeminarBase):
    pass

class SeminarUpdate(SeminarBase):
    pass

class SeminarOut(SeminarBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
