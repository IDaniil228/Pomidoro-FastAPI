from sqlalchemy.orm import  Mapped, mapped_column

from typing import Optional

from db import Base


class UserProfile(Base):
    __tablename__ = "UserProfile"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=True)
    password: Mapped[str] = mapped_column(nullable=True)
    name: Mapped[Optional[str]]
    email: Mapped[Optional[str]]
    google_access_token : Mapped[Optional[str]]
