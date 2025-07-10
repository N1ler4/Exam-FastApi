from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from auth.security import get_current_user
from database import get_db
import models, schemas

router = APIRouter(prefix="/references", tags=["Справки"])

@router.post("/", response_model=schemas.ReferenceOut)
def create_reference(data: schemas.ReferenceCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_ref = models.Reference(**data.dict())
    db.add(db_ref)
    db.commit()
    db.refresh(db_ref)
    return db_ref

@router.get("/", response_model=list[schemas.ReferenceOut])
def get_all_references(db: Session = Depends(get_db)):
    return db.query(models.Reference).all()

@router.delete("/{ref_id}", status_code=204)
def delete_reference(ref_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    ref = db.query(models.Reference).filter(models.Reference.id == ref_id).first()
    if not ref:
        raise HTTPException(status_code=404, detail="Reference not found")
    db.delete(ref)
    db.commit()
