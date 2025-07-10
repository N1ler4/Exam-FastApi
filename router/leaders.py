from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from auth.security import get_current_user
import models, schemas
from database import get_db

router = APIRouter(prefix="/leaders", tags=["Leaders"])

@router.post("/", response_model=schemas.LeaderOut)
def create_leader(leader: schemas.LeaderCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_leader = models.Leader(**leader.dict())
    db.add(db_leader)
    db.commit()
    db.refresh(db_leader)
    return db_leader

@router.get("/", response_model=list[schemas.LeaderOut])
def read_leaders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Leader).offset(skip).limit(limit).all()

@router.get("/{leader_id}", response_model=schemas.LeaderOut)
def read_leader(leader_id: int, db: Session = Depends(get_db)):
    db_leader = db.query(models.Leader).filter(models.Leader.id == leader_id).first()
    if not db_leader:
        raise HTTPException(status_code=404, detail="Leader not found")
    return db_leader

@router.put("/{leader_id}", response_model=schemas.LeaderOut)
def update_leader(leader_id: int, leader: schemas.LeaderUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_leader = db.query(models.Leader).filter(models.Leader.id == leader_id).first()
    if not db_leader:
        raise HTTPException(status_code=404, detail="Leader not found")
    for key, value in leader.dict().items():
        setattr(db_leader, key, value)
    db.commit()
    db.refresh(db_leader)
    return db_leader

@router.delete("/{leader_id}", status_code=204)
def delete_leader(leader_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_leader = db.query(models.Leader).filter(models.Leader.id == leader_id).first()
    if not db_leader:
        raise HTTPException(status_code=404, detail="Leader not found")
    db.delete(db_leader)
    db.commit()
