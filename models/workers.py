from sqlalchemy import Column, Integer, String
from database import Base

class Worker(Base):
    __tablename__ = "workers"

    id = Column(Integer, primary_key=True, index=True)
    worker_post = Column(String)
    worker_name = Column(String)
    worker_image = Column(String, nullable=True)
    worker_reception_day = Column(String)
    worker_reception_time = Column(String, nullable=False)
    worker_phone = Column(String, nullable=False)
    worker_email = Column(String, nullable=True)
    worker_bachelor = Column(String)
    worker_master = Column(String)
    academic_title = Column(String)
