from models.base import Base
from sqlalchemy.orm import Mapped, mapped_column


class Worker(Base):
    __tablename__ = "workers"

    name: Mapped[str]

    def __str__(self) -> str:
        return f"Worker(id = '{self.id}', name = '{self.name}')"
