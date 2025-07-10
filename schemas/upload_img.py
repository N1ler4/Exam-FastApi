from fastapi import UploadFile
from pydantic import BaseModel

class ConstituentUnitBase(BaseModel):
    img: UploadFile

class ConstituentUnitCreate(ConstituentUnitBase):
    pass

class ConstituentUnitOut(ConstituentUnitBase):
    id: int

    class Config:
        orm_mode = True