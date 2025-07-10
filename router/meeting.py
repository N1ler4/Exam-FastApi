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

router = APIRouter(prefix="/meetings", tags=["Meetings"])

@router.post("/", response_model=schemas.MeetingOut)
def create_meeting(meeting: schemas.MeetingCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_meeting = models.Meeting(**meeting.dict())
    db.add(db_meeting)
    db.commit()
    db.refresh(db_meeting)
    return db_meeting

@router.get("/", response_model=list[schemas.MeetingOut])
def read_meetings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Meeting).offset(skip).limit(limit).all()

@router.get("/{meeting_id}", response_model=schemas.MeetingOut)
def read_meeting(meeting_id: int, db: Session = Depends(get_db)):
    meeting = db.query(models.Meeting).filter(models.Meeting.id == meeting_id).first()
    if not meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")
    return meeting

@router.put("/{meeting_id}", response_model=schemas.MeetingOut)
def update_meeting(meeting_id: int, update: schemas.MeetingUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    meeting = db.query(models.Meeting).filter(models.Meeting.id == meeting_id).first()
    if not meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")
    for field, value in update.dict().items():
        setattr(meeting, field, value)
    db.commit()
    db.refresh(meeting)
    return meeting

@router.delete("/{meeting_id}", status_code=204)
def delete_meeting(meeting_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    meeting = db.query(models.Meeting).filter(models.Meeting.id == meeting_id).first()
    if not meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")
    db.delete(meeting)
    db.commit()
    return None
