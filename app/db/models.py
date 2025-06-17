from os import getenv

from sqlalchemy import BigInteger
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from dotenv import load_dotenv
load_dotenv()

engine = create_async_engine(getenv("DATABASE_URL"))
async_session = async_sessionmaker(engine)


class Base(DeclarativeBase, AsyncAttrs):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    tg_username: Mapped[str] = mapped_column()
    nickname: Mapped[str] = mapped_column()
    paid: Mapped[bool] = mapped_column(default=False)


async def migarte() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
