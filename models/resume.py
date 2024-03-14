from typing import Optional
from datetime import datetime

from models.base import Base
from enums.workload import Workload

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column


class Resume(Base):
    __tablename__ = "resumes"

    title: Mapped[str]
    salary: Mapped[Optional[int]]
    worktable: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id", ondelete="CASCADE"))
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now,
        onupdate=datetime.now)
