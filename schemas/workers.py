from pydantic import BaseModel, EmailStr
from typing import Optional

class WorkerBase(BaseModel):
    worker_reception_time: str
    worker_phone: str
    worker_email: Optional[EmailStr] = None

class WorkerCreate(WorkerBase):
    pass

class WorkerUpdate(WorkerBase):
    pass

class WorkerOut(BaseModel):
    id: int
    worker_post: str
    worker_name: str
    worker_image: Optional[str] = None
    worker_reception_day: str
    worker_reception_time: str
    worker_phone: str
    worker_email: Optional[EmailStr] = None
    worker_bachelor: str
    worker_master: str
    academic_title: str

    class Config:
        orm_mode = True
