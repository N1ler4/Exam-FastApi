from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class ShnqCategory(Base):
    __tablename__ = "shnq_categories"

    id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String, nullable=False)

    items = relationship("ShnqItem", back_populates="category", cascade="all, delete")


class ShnqItem(Base):
    __tablename__ = "shnq_items"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, nullable=False)
    name = Column(String, nullable=False)
    action = Column(String, nullable=False)

    category_id = Column(Integer, ForeignKey("shnq_categories.id"))
    category = relationship("ShnqCategory", back_populates="items")
