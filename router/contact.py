from fastapi import APIRouter, Form, UploadFile, File
from fastapi.responses import JSONResponse
import requests
from config import BOT_TOKEN, CHAT_ID

router = APIRouter(prefix="/contact", tags=["Contact"])

@router.post("/send")
async def send_contact_form(
    fullname: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    topic: str = Form(...),
    message: str = Form(...),
    file: UploadFile = File(None)
):
    text = (
        f"📩 Новое сообщение с сайта\n"
        f"👤 ФИО: {fullname}\n"
        f"📧 Email: {email}\n"
        f"📞 Телефон: {phone}\n"
        f"📌 Тема: {topic}\n"
        f"📝 Сообщение:\n{message}"
    )

    try:
        # Отправка текста
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            data={"chat_id": CHAT_ID, "text": text}
        )

        if file:
            telegram_file = {"document": (file.filename, await file.read())}
            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument",
                data={"chat_id": CHAT_ID, "caption": f"📎 Файл от {fullname}"},
                files=telegram_file
            )

        return JSONResponse({"detail": "Отправлено"}, status_code=200)

    except Exception as e:
        return JSONResponse({"detail": str(e)}, status_code=500)
