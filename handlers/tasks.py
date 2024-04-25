from fastapi import APIRouter, status
from schema.task import Task

from fixtures import tasks as fixtures_tasks

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get(
    "/all",
    response_model=list[Task]
)
async def get_tasks():
    return fixtures_tasks


@router.post(
    "/",
    response_model=Task
)
async def create_task(task: Task):
    fixtures_tasks.append(task)
    return task


@router.put(
    "/{task_id}",
    response_model=Task
)
async def update_task(task_id: int, name: str):
    for task in fixtures_tasks:
        if task["id"] == task_id:
            task["name"] = name
            return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int):
    for index, task in enumerate(fixtures_tasks):
        if task["id"] == task_id:
            del fixtures_tasks[index]
            return {"message": "task deleted"}
        return {"message": "task not found"}
