import asyncio
import logging

from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from app.handlers import user_router
from app.admin_handlers import admin_router
from app.db.models import migrate

from dotenv import load_dotenv
load_dotenv()

TOKEN = getenv("BOT_TOKEN")

async def main() -> None:
    await migrate()
    
    bot = Bot(
        token=TOKEN, 
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

    dp = Dispatcher()
    dp.include_router(user_router)
    dp.include_router(admin_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())