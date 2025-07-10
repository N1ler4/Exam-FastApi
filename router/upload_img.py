from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from auth.security import get_current_user
from database import get_db
import models, schemas

router = APIRouter(prefix="/units", tags=["Constituent Units"])

@router.post("/", response_model=schemas.ConstituentUnitOut)
def create_unit(unit: schemas.ConstituentUnitCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_unit = models.ConstituentUnits(**unit.dict())
    db.add(db_unit)
    db.commit()
    db.refresh(db_unit)
    return db_unit

@router.get("/", response_model=list[schemas.ConstituentUnitOut])
def get_all_units(db: Session = Depends(get_db)):
    return db.query(models.ConstituentUnits).all()

@router.get("/{unit_id}", response_model=schemas.ConstituentUnitOut)
def get_unit(unit_id: int, db: Session = Depends(get_db)):
    unit = db.query(models.ConstituentUnits).filter(models.ConstituentUnits.id == unit_id).first()
    if not unit:
        raise HTTPException(status_code=404, detail="Unit not found")
    return unit

@router.delete("/{unit_id}", status_code=204)
def delete_unit(unit_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    unit = db.query(models.ConstituentUnits).filter(models.ConstituentUnits.id == unit_id).first()
    if not unit:
        raise HTTPException(status_code=404, detail="Unit not found")
    db.delete(unit)
    db.commit()
