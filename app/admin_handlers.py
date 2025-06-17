from aiogram import F, Router, html
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.config import admin_ids
from app.keyboards import admin_menu_keyboard
from app.states import Admin
from app.db.requests import get_all_users, nickname_exists, set_paid

admin_router = Router()

@admin_router.message(Command("admin"))
async def admin(message: Message, state: FSMContext) -> None:
    if message.from_user.id in admin_ids:
        await message.answer(
            f"{html.bold(message.from_user.full_name)}, добро пожаловать в админ меню.", 
            reply_markup=admin_menu_keyboard
        )
        await state.set_state(Admin.menu)
    else:
        await message.answer("У вас нет прав!")

@admin_router.message(F.text == "👥 Список участников", Admin.menu)
async def users(message: Message) -> None:
    users = await get_all_users()
    cnt = 0
    answer = []

    for user in users:
        answer.append(f"Тг: @{user.tg_username}\nНикнейм: {user.nickname}\n" + 
                      f"Статус: {"Оплачен" if user.paid else "Неоплачен"}\n\n")
        cnt += 1
        
    answer.append(f"Кол-во участников: {cnt}")
        
    await message.answer("".join(answer), reply_markup=admin_menu_keyboard)

@admin_router.message(F.text == "🔄 Поменять статус", Admin.menu)
async def change_status(message: Message, state: FSMContext):
    await message.answer("Введите никнейм игрока, для которого хотите поменять статус.")
    await state.set_state(Admin.set_status)

@admin_router.message(F.text, Admin.set_status)
async def set_status(message: Message, state: FSMContext):
    nickname = message.text
    
    if await nickname_exists(nickname):
        await set_paid(nickname)
        await message.answer("Статус пользователя был сменен на 'Оплачен'.", reply_markup=admin_menu_keyboard)
        await state.set_state(Admin.menu)
    else:
        await message.answer("Пользователя с таким никнеймом не существует.\n" +
                              "Введите никнейм заново.")

    
