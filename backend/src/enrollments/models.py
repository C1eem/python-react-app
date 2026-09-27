import enum
from datetime import datetime

from sqlalchemy import ForeignKey, String, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column
from src.core.database import Base, TimestampMixin, intpk, str_100


class EnrollmentStatus(enum.Enum):
    active = "active"
    completed = "completed"
    dropped = "dropped"


class EnrollmentORM(Base):
    __tablename__ = "enrollments"
    id: Mapped[intpk]
    course_id: Mapped[int] = mapped_column(
        ForeignKey("courses.id", ondelete="CASCADE"),
        index=True,
    )
    student_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )
    status: Mapped[EnrollmentStatus] = mapped_column(default=EnrollmentStatus.active)
    enrolled_at: Mapped[datetime] = mapped_column(server_default=func.now())

    __table_args__ = (
        UniqueConstraint("course_id", "student_id", name="uq_course_student"),
    )


class LessonProgressORM(Base):
    __tablename__ = "lesson_progress"

    student_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        primary_key=True,
    )
    lesson_id: Mapped[int] = mapped_column(
        ForeignKey("lessons.id", ondelete="CASCADE"),
        primary_key=True,
    )
    completed_at: Mapped[datetime] = mapped_column(server_default=func.now())
