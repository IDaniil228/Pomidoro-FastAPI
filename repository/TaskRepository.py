from dataclasses import dataclass

from sqlalchemy.orm import Session
from sqlalchemy import insert, values, select

from models import Task


@dataclass
class TaskRepository:

    db_session : Session

    def get_all_user_tasks(self, user_id : int) -> list[Task]:
        query = select(Task).where(Task.user_id==user_id)
        with self.db_session() as session:
            return session.execute(query).scalars().all()

    def get_task(self, task_id : int) -> Task | None:
        query = select(Task).where(Task.id==task_id)
        with self.db_session() as session:
            return session.execute(query).scalar_one_or_none()

    def create_task(self, title : str, user_id : int) -> Task:
        query = insert(Task).values(
            title=title,
            user_id=user_id
        ).returning(Task.id)
        with self.db_session() as session:
            task_id : int = session.execute(query).scalar()
            session.commit()
            return self.get_task(task_id=task_id)