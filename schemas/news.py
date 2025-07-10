from pydantic import BaseModel
from typing import Optional

class NewsBase(BaseModel):
    title_uz: str
    title_ru: str
    title_en: str
    description_uz: Optional[str] = None
    description_ru: Optional[str] = None
    description_en: Optional[str] = None
    body_uz: Optional[str] = None
    body_ru: Optional[str] = None
    body_en: Optional[str] = None
    image: str
    video_url: Optional[str] = None
    date: str

class NewsCreate(NewsBase):
    pass

class NewsOut(NewsBase):
    id: int

    class Config:
        orm_mode = True
