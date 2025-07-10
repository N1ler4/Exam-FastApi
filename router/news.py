from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from auth.security import get_current_user
from database import get_db
import models, schemas

router = APIRouter(prefix="/news", tags=["News"])

@router.post("/", response_model=schemas.NewsOut)
def create_news(news: schemas.NewsCreate, db: Session = Depends(get_db) , user=Depends(get_current_user)):
    db_news = models.News(**news.dict())
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news

@router.get("/", response_model=list[schemas.NewsOut])
def get_all_news(db: Session = Depends(get_db)):
    return db.query(models.News).order_by(models.News.date.desc()).all()

@router.get("/{news_id}", response_model=schemas.NewsOut)
def get_news(news_id: int, db: Session = Depends(get_db)):
    news = db.query(models.News).filter(models.News.id == news_id).first()
    if not news:
        raise HTTPException(status_code=404, detail="News not found")
    return news

@router.delete("/{news_id}", status_code=204)
def delete_news(news_id: int, db: Session = Depends(get_db) , user=Depends(get_current_user)):
    news = db.query(models.News).filter(models.News.id == news_id).first()
    if not news:
        raise HTTPException(status_code=404, detail="News not found")
    db.delete(news)
    db.commit()
