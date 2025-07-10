from sqlalchemy import Column, Integer, String
from database import Base

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title_uz = Column(String, nullable=False)
    title_ru = Column(String, nullable=False)
    title_en = Column(String, nullable=False)
    description_uz = Column(String)
    description_ru = Column(String)
    description_en = Column(String)
    body_uz = Column(String)
    body_ru = Column(String)
    body_en = Column(String)
    image = Column(String, nullable=False)
    video_url = Column(String, nullable=True)
    date = Column(String, nullable=False)
