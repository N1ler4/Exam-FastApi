from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from auth.security import get_current_user
import models, schemas
from database import get_db

router = APIRouter(prefix="/workers", tags=["Workers"])

@router.post("/", response_model=schemas.WorkerOut)
def create_worker(worker: schemas.WorkerCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_worker = models.Worker(
        worker_post="",
        worker_name="",
        worker_image=None,
        worker_reception_day="",
        worker_reception_time=worker.worker_reception_time,
        worker_phone=worker.worker_phone,
        worker_email=worker.worker_email,
        worker_bachelor="",
        worker_master="",
        academic_title="",
    )
    db.add(db_worker)
    db.commit()
    db.refresh(db_worker)
    return db_worker

@router.get("/", response_model=list[schemas.WorkerOut])
def read_workers(db: Session = Depends(get_db)):
    return db.query(models.Worker).all()


@router.get("/{worker_id}", response_model=schemas.WorkerOut)
def read_worker(worker_id: int, db: Session = Depends(get_db)):
    db_worker = db.query(models.Worker).filter(models.Worker.id == worker_id).first()
    if not db_worker:
        raise HTTPException(status_code=404, detail="Worker not found")
    return db_worker

@router.put("/{worker_id}", response_model=schemas.WorkerOut)
def update_worker(worker_id: int, worker: schemas.WorkerUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_worker = db.query(models.Worker).filter(models.Worker.id == worker_id).first()
    if not db_worker:
        raise HTTPException(status_code=404, detail="Worker not found")
    db_worker.worker_reception_time = worker.worker_reception_time
    db_worker.worker_phone = worker.worker_phone
    db_worker.worker_email = worker.worker_email
    db.commit()
    db.refresh(db_worker)
    return db_worker

@router.delete("/{worker_id}", status_code=204)
def delete_worker(worker_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_worker = db.query(models.Worker).filter(models.Worker.id == worker_id).first()
    if not db_worker:
        raise HTTPException(status_code=404, detail="Worker not found")
    db.delete(db_worker)
    db.commit()
