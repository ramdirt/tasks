from fastapi import Depends
from database import get_db_session
from cache import get_redis_connection
from repository import TaskRepository, TaskCache, UserRepository
from service import TaskService, UserService, AuthService
from sqlalchemy.orm import Session

from settings import Settings


# Tasks
def get_tasks_repository(db_session: Session = Depends(get_db_session)) -> TaskRepository:
    return TaskRepository(db_session=db_session)


def get_tasks_cache_repository() -> TaskCache:
    redis_connection = get_redis_connection()
    return TaskCache(redis_connection)

def get_task_service(
        task_repository: TaskRepository = Depends(get_tasks_repository),
        task_cache: TaskCache = Depends(get_tasks_cache_repository)
) -> TaskService:
    return TaskService(task_repository=task_repository, task_cache=task_cache)


def get_users_repository(db_session: Session = Depends(get_db_session)) -> UserRepository:
    return UserRepository(db_session=db_session)


def get_auth_service(
        user_repository: UserRepository = Depends(get_users_repository)
) -> AuthService:
    return AuthService(
        user_repository=user_repository,
        settings= Settings()
        )


def get_user_service(
        user_repository: UserRepository = Depends(get_users_repository),
        auth_service: AuthService = Depends(get_auth_service)
) -> UserService:
    return UserService(
        user_repository=user_repository,
        auth_service=auth_service
    )
