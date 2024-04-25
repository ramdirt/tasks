from fastapi import APIRouter
from settings import Settings

router = APIRouter(prefix="/ping", tags=["ping"])

@router.get("/db")
async def ping_db():
    return {"message": "ok"}

@router.get("/app")
async def ping_app():
    return {"message": "ok"}


@router.get("/token")
async def token():
    settings = Settings()
    return {"message": settings.GOOGLE_TOKEN_ID}
