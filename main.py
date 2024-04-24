from fastapi import FastAPI
from handlers.ping import router as ping_router

app = FastAPI()

app.include_router(router=ping_router)
