from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from auth.security import get_current_user
from database import get_db
import models, schemas

router = APIRouter(prefix="/shnq", tags=["SHNQ"])

@router.post("/", response_model=schemas.ShnqCategoryOut)
def create_category(category: schemas.ShnqCategoryCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_category = models.ShnqCategory(category_name=category.category_name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)

    for item in category.items:
        db_item = models.ShnqItem(**item.dict(), category_id=db_category.id)
        db.add(db_item)
    db.commit()
    db.refresh(db_category)
    return db_category

@router.get("/", response_model=List[schemas.ShnqCategoryOut])
def get_all_shnq(db: Session = Depends(get_db)):
    return db.query(models.ShnqCategory).all()

@router.get("/{category_id}", response_model=schemas.ShnqCategoryOut)
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(models.ShnqCategory).filter(models.ShnqCategory.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category
