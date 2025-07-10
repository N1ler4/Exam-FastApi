from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LawBase(BaseModel):
    title: str
    content: str
    file_url: Optional[str] = None

class LawCreate(LawBase):
    pass

class LawUpdate(LawBase):
    pass

class LawOut(LawBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
