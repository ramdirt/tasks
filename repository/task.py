from sqlalchemy import select
from sqlalchemy.orm import Session

from database import Tasks, Categories, get_db_session

class TaskRepository():

    def __init__(self, db_session: Session):
        self.db_session = db_session


    def get_tasks(self):
        query = select(Tasks)

        with self.db_session() as session:
            tasks: list[Tasks] = session.execute(query).scalars().all()

        return tasks


    def get_task(self, task_id: int) -> Tasks | None:
        query = select(Tasks).where(Tasks.id == task_id)

        with self.db_session() as session:
            task: Tasks = session.execute(query).scalar_one_or_none()

        return task
    

    def create_task(self, task: Tasks) -> None:
        with self.db_session() as session:
            session.add(task)
            session.commit()


    def delete_task(self, task_id: int) -> None:
        query = delete(Tasks).where(Tasks.id == task_id)

        with self.db_session() as session:
            session.execute(query)
            session.commit()

    def get_task_by_category_id(self, category_name: int) -> list[Tasks] | None:
        query = select(Tasks).join(Categories, Tasks.category_id == Categories.id).where(Tasks.category_name == category_name)

        with self.db_session() as session:
            tasks: list[Tasks] = session.execute(query).scalars().all()

        return tasks



def get_tasks_repository() -> TaskRepository:
    db_session = get_db_session()
    return TaskRepository(db_session)