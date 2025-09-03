from dataclasses import dataclass

from Schema.task import TaskSchema

from repository import TaskRepository


@dataclass
class TaskService:

    task_repository: TaskRepository

    def get_tasks(self, user_id : int) -> list[TaskSchema]:
        tasks = self.task_repository.get_all_user_tasks(user_id=user_id)
        task_list = [TaskSchema.model_validate(task) for task in tasks]
        return task_list

    def create_task(self, title : str, user_id : int) -> TaskSchema:
        task = self.task_repository.create_task(title=title, user_id=user_id)
        return TaskSchema(id=task.id, title=task.title, user_id=user_id)