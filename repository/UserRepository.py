from dataclasses import dataclass

from sqlalchemy import select, insert
from sqlalchemy.orm import Session

from Schema import UserLoginSchema, UserCreateSchema
from db.accessor import session
from models import UserProfile

@dataclass
class UserRepository:

    db_session : Session

    def create_user(self, user : UserCreateSchema) -> UserProfile:
        query = insert(UserProfile).values(
            **user.model_dump()
        ).returning(UserProfile.id)
        with self.db_session() as session:
            user_id : int = session.execute(query).scalar()
            session.commit()
            return self.get_user(user_id)

    def get_all_user(self) -> list[UserProfile]:
        query = select(UserProfile)
        with self.db_session() as session:
            users = session.execute(query).scalars().all()
        return users


    def get_user(self, user_id : int) -> UserProfile | None:
        query = select(UserProfile).where(UserProfile.id==user_id)
        with self.db_session() as session:
            return session.execute(query).scalar_one_or_none()

    def get_user_by_username(self, username: str) -> UserProfile | None:
        query = select(UserProfile).where(UserProfile.username==username)
        with self.db_session() as session:
            return session.execute(query).scalar_one_or_none()

    def get_user_by_email(self, email : str) -> UserProfile | None:
        query = select(UserProfile).where(UserProfile.email==email)
        with self.db_session() as session:
            return session.execute(query).scalar_one_or_none()

