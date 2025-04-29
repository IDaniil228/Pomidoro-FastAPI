from sqlalchemy import ForeignKey

from sqlalchemy.orm import mapped_column, Mapped, declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = "Users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    second_name: Mapped[str] = mapped_column(nullable=True)
    age: Mapped[int]


class Resume(Base):
    __tablename__ = "Resumes"

    id: Mapped[int] = mapped_column(primary_key=True)
    title : Mapped[str]
    description: Mapped[str]
    user_id : Mapped[int] = mapped_column(ForeignKey("Users.id"))