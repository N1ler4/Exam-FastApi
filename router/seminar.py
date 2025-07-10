from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from auth.security import get_current_user
from database import SessionLocal
import models, schemas

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter(prefix="/seminars", tags=["seminars"])

@router.post("/", response_model=schemas.SeminarOut)
def create_seminar(seminar: schemas.SeminarCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_seminar = models.Seminar(**seminar.dict())
    db.add(db_seminar)
    db.commit()
    db.refresh(db_seminar)
    return db_seminar

@router.get("/", response_model=list[schemas.SeminarOut])
def read_seminars(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Seminar).offset(skip).limit(limit).all()

@router.get("/{seminar_id}", response_model=schemas.SeminarOut)
def read_seminar(seminar_id: int, db: Session = Depends(get_db)):
    seminar = db.query(models.Seminar).filter(models.Seminar.id == seminar_id).first()
    if not seminar:
        raise HTTPException(status_code=404, detail="seminar not found")
    return seminar

@router.put("/{seminar_id}", response_model=schemas.SeminarOut)
def update_seminar(seminar_id: int, update: schemas.SeminarUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    seminar = db.query(models.Seminar).filter(models.Seminar.id == seminar_id).first()
    if not seminar:
        raise HTTPException(status_code=404, detail="seminar not found")
    for field, value in update.dict().items():
        setattr(seminar, field, value)
    db.commit()
    db.refresh(seminar)
    return seminar

@router.delete("/{seminar_id}", status_code=204)
def delete_seminar(seminar_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    seminar = db.query(models.Seminar).filter(models.Seminar.id == seminar_id).first()
    if not seminar:
        raise HTTPException(status_code=404, detail="seminar not found")
    db.delete(seminar)
    db.commit()
    return None
