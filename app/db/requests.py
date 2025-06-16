from sqlalchemy import select

from app.db.models import async_session
from app.db.models import User

async def create_user(tg_id: int, nickname: str) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        
        if not user:
            session.add(User(tg_id=tg_id, nickname=nickname))
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
        nickname = await session.scalar(select(User.nickname).where(User.nickname == nickname))
        return nickname is not None