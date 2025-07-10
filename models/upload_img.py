

from sqlalchemy import Column, Integer, String


class ConstituentUnits:
    
    __tablename__ = "constituent_units"
    
    id = Column(Integer, primary_key=True, index=True)
    img = Column(String, nullable=False)
    