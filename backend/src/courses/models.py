import enum

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from src.core.database import Base, TimestampMixin, intpk, str_100


class CourseStatus(enum.Enum):
    draft = "draft"
    published = "published"
    archived = "archived"


class LessonType(enum.Enum):
    video = "video"
    text = "text"
    quiz = "quiz"
    assignment = "assignment"


class CourseORM(Base):
    __tablename__ = "courses"

    id: Mapped[intpk]
    author_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="RESTRICT"),
        index=True,
    )
    title: Mapped[str_100]
    description: Mapped[str | None]
    cover_url: Mapped[str | None]
    status: Mapped[CourseStatus] = mapped_column(default=CourseStatus.draft)


class ModuleORM(Base):
    __tablename__ = "modules"

    id: Mapped[intpk]
    course_id: Mapped[int] = mapped_column(
        ForeignKey("course.id", ondelete="CASCADE"),
        index=True,
    )
    title: Mapped[str_100]
    position: Mapped[int] = mapped_column(default=0)


class LessonORM(Base):
    __tablename__ = "lessons"

    id: Mapped[intpk]
    module_id: Mapped[int] = mapped_column(
        ForeignKey("modules.id", ondelete="CASCADE"),
        index=True,
    )
    title: Mapped[str_100]
    type: Mapped[LessonType]
    position: Mapped[int] = mapped_column(default=0)
    is_published: Mapped[bool] = mapped_column(default=False)


class LessonVideoORM(Base):
    __tablename__ = "lesson_videos"

    lesson_id: Mapped[int] = mapped_column(
        ForeignKey("lessons.id", ondelete="CASCADE"),
        primary_key=True,
    )
    video_url: Mapped[str]
    duration: Mapped[int | None]


class LessonTextORM(Base):
    __tablename__ = "lesson_texts"

    lesson_id: Mapped[int] = mapped_column(
        ForeignKey("lesson.id", ondelete="CASCADE"),
        primary_key=True,
    )
    content: Mapped[str]


class LessonFileORM(Base):
    __tablename__ = "lesson_files"

    id: Mapped[intpk]
    lesson_id: Mapped[int] = mapped_column(
        ForeignKey("lessons.id", ondelete="CASCADE"),
        index=True,
    )
    file_url: Mapped[str]
    file_name: Mapped[str] = mapped_column(String(255))
    mime_type: Mapped[str_100 | None]
