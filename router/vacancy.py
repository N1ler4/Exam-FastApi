from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from auth.security import get_current_user
from database import get_db
import models, schemas

router = APIRouter(prefix="/vacancies", tags=["Vacancies"])

@router.post("/", response_model=schemas.VacancyOut)
def create_vacancy(vacancy: schemas.VacancyCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    db_vacancy = models.Vacancy(**vacancy.dict())
    db.add(db_vacancy)
    db.commit()
    db.refresh(db_vacancy)
    return db_vacancy

@router.get("/", response_model=list[schemas.VacancyOut])
def read_vacancies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(models.Vacancy).offset(skip).limit(limit).all()

@router.get("/{vacancy_id}", response_model=schemas.VacancyOut)
def read_vacancy(vacancy_id: int, db: Session = Depends(get_db) ):
    vacancy = db.query(models.Vacancy).filter(models.Vacancy.id == vacancy_id).first()
    if not vacancy:
        raise HTTPException(status_code=404, detail="Vacancy not found")
    return vacancy

@router.put("/{vacancy_id}", response_model=schemas.VacancyOut)
def update_vacancy(vacancy_id: int, data: schemas.VacancyUpdate, db: Session = Depends(get_db) , user=Depends(get_current_user)):
    vacancy = db.query(models.Vacancy).filter(models.Vacancy.id == vacancy_id).first()
    if not vacancy:
        raise HTTPException(status_code=404, detail="Vacancy not found")
    for key, value in data.dict(exclude_unset=True).items():
        setattr(vacancy, key, value)
    db.commit()
    db.refresh(vacancy)
    return vacancy

@router.delete("/{vacancy_id}", status_code=204)
def delete_vacancy(vacancy_id: int, db: Session = Depends(get_db) , user=Depends(get_current_user)):
    vacancy = db.query(models.Vacancy).filter(models.Vacancy.id == vacancy_id).first()
    if not vacancy:
        raise HTTPException(status_code=404, detail="Vacancy not found")
    db.delete(vacancy)
    db.commit()
