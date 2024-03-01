from sqlalchemy import create_engine, ForeignKey, select
from sqlalchemy.orm import as_declarative, declared_attr, mapped_column, Mapped, Session

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)


@as_declarative()
class AbstractModel:
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)

    @classmethod
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower() + 's'


class User(AbstractModel):
    name: Mapped[str]
    fullname: Mapped[str]


class Address(AbstractModel):
    __tablename__ = "addresses"
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    email: Mapped[str] = mapped_column(nullable=False)


user = User(name="Dimas", fullname="Dimas Hasiuk")
address = Address(user_id="1", email="example.com")

with Session(engine) as session:
    with session.begin():
        AbstractModel.metadata.create_all(engine)
        session.add(user)
        session.add(address)
    with session.begin():
        res = session.execute(select(User).where(User.id == 1))
        user = res.scalar()
        print(user.name)
