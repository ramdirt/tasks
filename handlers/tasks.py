from typing import Annotated
from dependecy import get_tasks_repository

from fastapi import APIRouter, status, Depends
from schema.task import TaskSchema
from repository import TaskRepository

from fixtures import tasks as fixtures_tasks

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get(
    "/all",
    response_model=list[TaskSchema]
)
async def get_tasks(task_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]):
    tasks = task_repository.get_tasks()

    return tasks


@router.post(
    "/",
    response_model=TaskSchema
)
async def create_task(
    task: TaskSchema,
    task_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]
):

    task_id = task_repository.create_task(task)
    task.id = task_id

    return task


@router.put(
    "/{task_id}",
    response_model=TaskSchema
)
async def update_task(task_id: int, name: str):
    pass


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int):
    pass


@router.patch(
        "/{task_id}",
        response_model=TaskSchema
        )
async def patch_task(
    task_id: int,
    name: str,
    task_repository: Annotated[TaskRepository, Depends(get_tasks_repository)]
):
    return task_repository.update_task_name(task_id, name)