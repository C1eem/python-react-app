import enum

from sqlalchemy import ForeignKey, String
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
    email: Mapped[str_100] = mapped_column(unique=True, index=True)
    hashed_password: Mapped[str]
    first_name: Mapped[str_100]
    last_name: Mapped[str_100]
    middle_name: Mapped[str_100 | None]
    role: Mapped[UserRole] = mapped_column(default=UserRole.student)
    is_active: Mapped[bool] = mapped_column(default=True)


class ParentStudentORM(Base):
    __tablename__ = "parent_student"

    parent_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        primary_key=True,
    )
    student_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        primary_key=True,
    )
