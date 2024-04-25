from fastapi import APIRouter, status
from schema.task import Task
from database import get_db_connection

from fixtures import tasks as fixtures_tasks

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get(
    "/all",
    response_model=list[Task]
)
async def get_tasks():
    result: list[Task] = []

    cursor = get_db_connection().cursor()
    tasks = cursor.execute("SELECT * FROM tasks").fetchall()
    for task in tasks:
        result.append(Task(
            id=task[0],
            name=task[1],
            pomodoro_count=task[2],
            category_id=task[3]
        ))

    return fixtures_tasks


@router.post(
    "/",
    response_model=Task
)
async def create_task(task: Task):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO tasks (id, name, pomodoro_count, category_id) VALUES (?,?,?,?)",
        (task.id, task.name, task.pomodoro_count, task.category_id)
    )
    connection.commit()
    connection.close()

    fixtures_tasks.append(task)
    return task


@router.put(
    "/{task_id}",
    response_model=Task
)
async def update_task(task_id: int, name: str):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE tasks SET name =? WHERE id =?", (name, task_id))
    connection.commit()
    connection.close()


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
