from fastapi import APIRouter, Depends, Query
from fastapi import Depends, HTTPException, Query
from sqlalchemy.orm import Session
from auth.security import get_current_user
from database import SessionLocal
import models, schemas

router = APIRouter(prefix="/submenus", tags=["SubMenus"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/submenus/", response_model=schemas.SubMenuOut)
def create_submenu(submenu: schemas.SubMenuCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    menu = db.query(models.Menu).filter(models.Menu.id == submenu.menu_id).first()
    if not menu:
        raise HTTPException(status_code=400, detail="Menu not found")
    db_submenu = models.SubMenu(**submenu.dict())
    db.add(db_submenu)
    db.commit()
    db.refresh(db_submenu)
    return {"id": db_submenu.id, "submenu": db_submenu.submenu_uz, "menu_id": db_submenu.menu_id}

@router.get("/submenus/", response_model=list[schemas.SubMenuOut])
def read_submenus(lang: str = Query("uz", enum=["uz", "ru", "en"]), db: Session = Depends(get_db)):
    submenus = db.query(models.SubMenu).all()
    return [{"id": s.id, "submenu": getattr(s, f"submenu_{lang}"), "menu_id": s.menu_id} for s in submenus]

@router.get("/submenus/{submenu_id}", response_model=schemas.SubMenuOut)
def read_submenu(submenu_id: int, lang: str = Query("uz", enum=["uz", "ru", "en"]), db: Session = Depends(get_db)):
    submenu = db.query(models.SubMenu).filter(models.SubMenu.id == submenu_id).first()
    if not submenu:
        raise HTTPException(status_code=404, detail="SubMenu not found")
    return {"id": submenu.id, "submenu": getattr(submenu, f"submenu_{lang}"), "menu_id": submenu.menu_id}

@router.put("/submenus/{submenu_id}", response_model=schemas.SubMenuOut)
def update_submenu(submenu_id: int, submenu_update: schemas.SubMenuUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    submenu = db.query(models.SubMenu).filter(models.SubMenu.id == submenu_id).first()
    if not submenu:
        raise HTTPException(status_code=404, detail="SubMenu not found")
    # Menu mavjudligini tekshirish (agar menu_id o'zgargan bo'lsa)
    menu = db.query(models.Menu).filter(models.Menu.id == submenu_update.menu_id).first()
    if not menu:
        raise HTTPException(status_code=400, detail="Menu not found")
    for field, value in submenu_update.dict().items():
        setattr(submenu, field, value)
    db.commit()
    db.refresh(submenu)
    return {"id": submenu.id, "submenu": submenu.submenu_uz, "menu_id": submenu.menu_id}

@router.delete("/submenus/{submenu_id}", status_code=204)
def delete_submenu(submenu_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    submenu = db.query(models.SubMenu).filter(models.SubMenu.id == submenu_id).first()
    if not submenu:
        raise HTTPException(status_code=404, detail="SubMenu not found")
    db.delete(submenu)
    db.commit()
    return None