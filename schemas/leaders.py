from pydantic import BaseModel, EmailStr
from typing import Optional

class LeaderBase(BaseModel):
    leader_position: str
    leader_full_name: str
    leader_image: str
    leader_phone: str
    leader_email: EmailStr
    day_of_week: str
    graduation_info: Optional[str] = None

class LeaderCreate(LeaderBase):
    pass

class LeaderUpdate(LeaderBase):
    pass

class LeaderOut(LeaderBase):
    id: int

    class Config:
        orm_mode = True
