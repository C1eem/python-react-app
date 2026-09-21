import enum

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from src.core.database import Base, TimestampMixin, intpk, str_100


class UserRole(enum.Enum):
    admin = "admin"
    parent = "parent"
    student = "student"
    tutor = "tutor"


class UserORM(TimestampMixin, Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    email: Mapped[str_100]
    hashed_password: Mapped[str]
    first_name: Mapped[str_100]
    last_name: Mapped[str_100]
    middle_name: Mapped[str_100 | None]
    role: Mapped[UserRole]
