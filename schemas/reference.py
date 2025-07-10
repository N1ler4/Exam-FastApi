from fastapi import UploadFile
from pydantic import BaseModel


class ReferenceBase(BaseModel):
    title: str
    file_url: UploadFile  

class ReferenceCreate(ReferenceBase):
    pass

class ReferenceOut(ReferenceBase):
    id: int

    class Config:
        orm_mode = True


class ReferenceUpdate(ReferenceBase):
    pass
