from typing import Iterable

from sqlalchemy import select, update

from app.db.models import async_session
from app.db.models import User

async def create_user(tg_id: int, tg_username: str, nickname: str) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        
        if not user:
            session.add(User(tg_id=tg_id, tg_username=tg_username, nickname=nickname))
            await session.commit()

async def get_user(tg_id: int) -> User:
    async with async_session() as session:
        return await session.scalar(select(User).where(User.tg_id == tg_id))
    
async def delete_user(tg_id: int) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if user:
            await session.delete(user)
            await session.commit()

async def user_exists(tg_id: int) -> bool:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        return user is not None
    
async def nickname_exists(nickname: str) -> bool:
    async with async_session() as session:
        return await session.scalar(select(User.nickname).where(User.nickname == nickname))
        return user is not None
    
async def get_all_users() -> Iterable[User]:
    async with async_session() as session:
        return await session.scalars(select(User))
    
async def set_paid(nickname: str) -> None:
    async with async_session() as session:
        await session.execute(update(User).values(paid=True).where(User.nickname == nickname))
        await session.commit()