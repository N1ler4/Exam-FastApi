from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class VacancyBase(BaseModel):
    title: str
    description: Optional[str] = None
    requirements: Optional[str] = None
    is_active: Optional[bool] = True

class VacancyCreate(VacancyBase):
    pass

class VacancyUpdate(VacancyBase):
    pass

class VacancyOut(VacancyBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
