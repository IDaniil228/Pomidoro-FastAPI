from dataclasses import dataclass

from Schema.TaskCreateSchema import TaskCreateSchema
from models import Task
from repository import TaskRepository


@dataclass
class TaskService:

    task_repository: TaskRepository

    def get_tasks(self, user_id : int) -> list[TaskCreateSchema]:
        tasks = self.task_repository.get_all_user_tasks(user_id=user_id)
        task_list = [TaskCreateSchema.model_validate(task) for task in tasks]
        return task_list

    def create_task(self, title : str, user_id : int) -> TaskCreateSchema:
        task = self.task_repository.create_task(title=title, user_id=user_id)
        return TaskCreateSchema(id=task.id, title=task.title, user_id=user_id)