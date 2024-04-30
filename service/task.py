from dataclasses import dataclass
from repository import TaskRepository, TaskCache
from schema import TaskSchema, TaskCreateSchema


@dataclass
class TaskService:
    task_repository: TaskRepository
    task_cache: TaskCache

    def get_tasks(self) -> list[TaskSchema]:
        if tasks := self.task_cache.get_tasks():
            return tasks
    
        tasks = self.task_repository.get_tasks()
        tasks_schema = [TaskSchema.model_validate(task) for task in tasks]
        self.task_cache.set_tasks(tasks_schema)

        return tasks
    

    def get_task(self, task_id: int) -> TaskSchema:
        task = self.task_repository.get_task(task_id)
        return task
    

    def create_task(self, task: TaskCreateSchema, user_id: int) -> int:
        task_id = self.task_repository.create_task(task=task, user_id=user_id)

        return self.get_task(task_id)
    
    def delete_task(self, task_id):
        self.task_repository.delete_task(task_id)


    def update_task(self, task_id: int, name: str) -> TaskSchema:
        task = self.task_repository.update_name(task_id, name)
        
        return task
    
