from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from auth.security import get_current_user
from database import get_db
import models, schemas
from typing import List

router = APIRouter(prefix="/construction", tags=["Construction Regulations"])

@router.post("/", response_model=schemas.ConstructionRegulationOut)
def create_regulation(data: schemas.ConstructionRegulationCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    reg = models.ConstructionRegulation(**data.dict())
    db.add(reg)
    db.commit()
    db.refresh(reg)
    return reg

@router.get("/", response_model=List[schemas.ConstructionRegulationOut])
def get_all_regulations(db: Session = Depends(get_db)):
    return db.query(models.ConstructionRegulation).all()

@router.get("/{reg_id}", response_model=schemas.ConstructionRegulationOut)
def get_one_regulation(reg_id: int, db: Session = Depends(get_db)):
    reg = db.query(models.ConstructionRegulation).filter(models.ConstructionRegulation.id == reg_id).first()
    if not reg:
        raise HTTPException(status_code=404, detail="Regulation not found")
    return reg

@router.put("/{reg_id}", response_model=schemas.ConstructionRegulationOut)
def update_regulation(reg_id: int, update_data: schemas.ConstructionRegulationUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    reg = db.query(models.ConstructionRegulation).filter(models.ConstructionRegulation.id == reg_id).first()
    if not reg:
        raise HTTPException(status_code=404, detail="Regulation not found")
    for key, value in update_data.dict().items():
        setattr(reg, key, value)
    db.commit()
    db.refresh(reg)
    return reg

@router.delete("/{reg_id}", status_code=204)
def delete_regulation(reg_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    reg = db.query(models.ConstructionRegulation).filter(models.ConstructionRegulation.id == reg_id).first()
    if not reg:
        raise HTTPException(status_code=404, detail="Regulation not found")
    db.delete(reg)
    db.commit()
