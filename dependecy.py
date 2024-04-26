from database import get_db_session
from repository import TaskRepository


def get_tasks_repository() -> TaskRepository:
    db_session = get_db_session()
    return TaskRepository(db_session)