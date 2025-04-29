from sqlalchemy import select
from sqlalchemy.orm import Session

from db import get_db_session, User


class UserRepository:

    def __init__(self, db_session : Session):
        self.db_session = db_session

    def get_all_user(self) -> list[User]:
        query = select(User)
        with self.db_session() as session:
            users = session.execute(query).scalars().all()
        return users

    def create_user(self):
        pass
