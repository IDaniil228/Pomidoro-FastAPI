from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from db import Base
from models import UserProfile


class Task(Base):
    __tablename__ = "Task"

    id : Mapped[int] = mapped_column(primary_key=True)
    title : Mapped[str] = mapped_column(nullable=False)
    user_id : Mapped[int] = mapped_column(ForeignKey("UserProfile.id"), nullable=False)
