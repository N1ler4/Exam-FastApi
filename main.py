from fastapi import FastAPI
from database import Base, engine
from router import (users, menu, submenu, workers, leaders,
                    vacancy, law, shnq, con_regulation, reference, upload_img, news, contact, meeting, event, seminar)
from auth.auth import router as auth_router


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(auth_router)
app.include_router(menu.router)
app.include_router(submenu.router)
app.include_router(workers.router)
app.include_router(leaders.router)
app.include_router(vacancy.router)
app.include_router(law.router)
app.include_router(shnq.router)
app.include_router(con_regulation.router)
app.include_router(reference.router)
app.include_router(upload_img.router)
app.include_router(news.router)
app.include_router(contact.router)
app.include_router(meeting.router)
app.include_router(event.router)
app.include_router(seminar.router)