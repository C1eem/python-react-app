import enum

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from src.core.database import Base, TimestampMixin, intpk, str_100


class TaskType(enum.Enum):
    quiz = "quiz"
    essay = "essay"
    file = "file"
    manual = "manual"


class QuestionType(enum.Enum):
    single = "single"
    multiple = "multiple"
    text = "text"


class TaskORM(TimestampMixin, Base):
    __tablename__ = "tasks"

    id: Mapped[intpk]
    lesson_id: Mapped[int] = mapped_column(
        ForeignKey("lesson.id", ondelete="CASCADE"),
        index=True,
    )
    type: Mapped[TaskType]
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None]
    max_score: Mapped[int | None]
    is_required: Mapped[bool] = mapped_column(default=False)
    position: Mapped[int] = mapped_column(default=0)


class QuestoinORM(TimestampMixin, Base):
    __tablename__ = "questions"

    id: Mapped[intpk]
    task_id: Mapped[int] = mapped_column(
        ForeignKey("tasks.id", ondelete="CASCADE"),
        index=True,
    )
    type: Mapped[QuestionType]
    text: Mapped[str]
    points: Mapped[int] = mapped_column(default=1)
    position: Mapped[int] = mapped_column(default=0)


class QuestionOptionORM(Base):
    __tablename__ = "question_options"

    id: Mapped[intpk]
    question_id: Mapped[int] = mapped_column(
        ForeignKey("questions.id", ondelete="CASCADE"),
        index=True,
    )
    text: Mapped[str]
    is_correct: Mapped[bool] = mapped_column(default=False)
    position: Mapped[int] = mapped_column(default=0)
