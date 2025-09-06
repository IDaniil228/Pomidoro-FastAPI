from dataclasses import dataclass

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select

from models import Task


@dataclass
class TaskRepository:

    db_session : AsyncSession

    async def get_all_user_tasks(self, user_id : int) -> list[Task]:
        query = select(Task).where(Task.user_id==user_id)
        async with self.db_session as session:
            return (await session.execute(query)).scalars().all()

    async def get_task(self, task_id : int) -> Task | None:
        query = select(Task).where(Task.id==task_id)
        async with self.db_session as session:
            return (await session.execute(query)).scalar_one_or_none()

    async def create_task(self, title : str, user_id : int) -> Task:
        query = insert(Task).values(
            title=title,
            user_id=user_id
        ).returning(Task.id)
        async with self.db_session as session:
            task_id : int = (await session.execute(query)).scalar()
            await session.commit()
            return await self.get_task(task_id=task_id)