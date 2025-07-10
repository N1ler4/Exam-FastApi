from pydantic import BaseModel
from typing import List, Optional

class ShnqItemBase(BaseModel):
    code: str
    name: str
    action: str

class ShnqItemCreate(ShnqItemBase):
    pass

class ShnqItemOut(ShnqItemBase):
    id: int

    class Config:
        orm_mode = True

class ShnqCategoryBase(BaseModel):
    category_name: str

class ShnqCategoryCreate(ShnqCategoryBase):
    items: List[ShnqItemCreate]

class ShnqCategoryOut(ShnqCategoryBase):
    id: int
    items: List[ShnqItemOut]

    class Config:
        orm_mode = True
