import enum
from datetime import datetime

from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from src.core.database import Base, TimestampMixin, intpk, str_100


class SubmissionStatus(enum.Enum):
    draft = "draft"
    submitted = "submitted"
    graded = "graded"
    returned = "returned"


class SubmissionsORM(TimestampMixin, Base):
    __tablename__ = "submissions"

    id: Mapped[intpk]
    task_id: Mapped[int] = mapped_column(
        ForeignKey("tasks.id", ondelete="CASCADE"),
        index=True,
    )
    student_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        index=True,
    )
    status: Mapped[SubmissionStatus] = mapped_column(default=SubmissionStatus.draft)
    score: Mapped[int | None]
    feedback: Mapped[str | None]
    graded_by: Mapped[int | None] = mapped_column(
        ForeignKey("users.id", ondelete="SET NULL")
    )
    submitted_at: Mapped[datetime | None]
    graded_at: Mapped[datetime | None]

    __table_args__ = UniqueConstraint("task_id", "student_id", name="uq_task_student")


class SubmissionAnswerORM(Base):
    __tablename__ = "submission_answers"

    id: Mapped[intpk]
    sumbission_id: Mapped[int] = mapped_column(
        ForeignKey("submissions.id", ondelete="CASCADE"),
        index=True,
    )
    question_id: Mapped[int] = mapped_column(
        ForeignKey("questions.id", ondelete="CASCADE"),
        index=True,
    )
    answer_text: Mapped[str | None]

    __table_args__ = UniqueConstraint(
        "submission_id", "question_id", name="uq_submission_question"
    )


class SubmissionAnswerOption(Base):
    __tablename__ = "submission_answer_options"

    submission_answer_id: Mapped[int] = mapped_column(
        ForeignKey("submission_answers.id", ondelete="CASCADE"),
        index=True,
    )
    option_id: Mapped[int] = mapped_column(
        ForeignKey("question_options.id", ondelete="CASCADE"),
        index=True,
    )


class SubmissionFileORM(Base):
    __tablename__ = "submission_files"

    id: Mapped[intpk]
    submission_id: Mapped[int] = mapped_column(
        ForeignKey("submissions.id", ondelete="CASCADE"),
        index=True,
    )
    file_url: Mapped[str]
    file_name: Mapped[str] = mapped_column(String(255))
    mime_type: Mapped[str_100 | None]
