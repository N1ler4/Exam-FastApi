from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from auth.security import get_current_user
from database import get_db
import models, schemas

router = APIRouter(prefix="/laws", tags=["Laws"])

@router.post("/", response_model=schemas.LawOut)
def create_law(law: schemas.LawCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_law = models.Law(**law.dict())
    db.add(db_law)
    db.commit()
    db.refresh(db_law)
    return db_law

@router.get("/", response_model=list[schemas.LawOut])
def read_laws(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Law).offset(skip).limit(limit).all()

@router.get("/{law_id}", response_model=schemas.LawOut)
def read_law(law_id: int, db: Session = Depends(get_db)):
    law = db.query(models.Law).filter(models.Law.id == law_id).first()
    if not law:
        raise HTTPException(status_code=404, detail="Law not found")
    return law

@router.put("/{law_id}", response_model=schemas.LawOut)
def update_law(law_id: int, law_update: schemas.LawUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_law = db.query(models.Law).filter(models.Law.id == law_id).first()
    if not db_law:
        raise HTTPException(status_code=404, detail="Law not found")
    for key, value in law_update.dict(exclude_unset=True).items():
        setattr(db_law, key, value)
    db.commit()
    db.refresh(db_law)
    return db_law

@router.delete("/{law_id}", status_code=204)
def delete_law(law_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_law = db.query(models.Law).filter(models.Law.id == law_id).first()
    if not db_law:
        raise HTTPException(status_code=404, detail="Law not found")
    db.delete(db_law)
    db.commit()
