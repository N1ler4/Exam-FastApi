from sqlalchemy import Column, Integer, String
from database import Base

class Leader(Base): 
    __tablename__ = "leaders"

    id = Column(Integer, primary_key=True, index=True)
    leader_position = Column(String, nullable=False)
    leader_full_name = Column(String, nullable=False)
    leader_image = Column(String, nullable=False)
    leader_phone = Column(String, nullable=False)
    leader_email = Column(String, nullable=False)  # исправлено с EmailStr на String
    day_of_week = Column(String(15), nullable=False)
    graduation_info = Column(String, nullable=True)
