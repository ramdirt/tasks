from fastapi import APIRouter
from settings import Settings

router = APIRouter(prefix="/ping", tags=["ping"])

@router.get("/db")
async def ping_db():
    settings = Settings()
    settings.GOOGLE_TOKEN_ID

    return {"message": "ok"}

@router.get("/app")
async def ping_app():
    return {"message": "ok"}
