from sqlalchemy import Column, Integer, String
from database import Base

class ConstructionRegulation(Base):
    __tablename__ = "construction_regulations"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, nullable=False)     # Например: СНиП 2.01.07-85
    name = Column(String, nullable=False)     # Название регламента
    action = Column(String, nullable=False)   # Статус (например: "Yangi", "O‘zgartirilgan", "Bekor qilingan")
