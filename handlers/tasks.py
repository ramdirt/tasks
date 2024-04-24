from fastapi import APIRouter

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("/all")
async def get_tasks_two():
    return {"message": "ok"}


@router.post("/")
async def add_tasks_two():
    return {"message": "ok"}
