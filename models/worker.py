from models.base import Base
from sqlalchemy.orm import Mapped, mapped_column


class Worker(Base):
    __tablename__ = "workers"

    name: Mapped[str]
