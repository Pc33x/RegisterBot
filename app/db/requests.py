from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_session

from app.db.models import User

async def create_user(tg_id: int, nickname: str) -> None:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        
        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()

            

