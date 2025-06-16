from aiogram import F, Router, html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from app.keyboards import menu_keyboard, withdraw_keyboard
from app.states import Register
from app.db.requests import (
    create_user, 
    user_exists,
    nickname_exists,
    delete_user,
    get_user
)

router = Router()

@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer(
        f"Здравствуй, дорогой {html.bold(message.from_user.full_name)}!\n" +
        f"\nДобро пожаловать в бота от группы {html.link("Панамера", "https://t.me/panamera221")}.\n" +
        f"Для регистрации на {html.italic("турнир")} просто нажми {html.bold("кнопку")} ниже.",
        reply_markup=menu_keyboard
    )
    
@router.message(F.text == "Зарегистрироваться")
async def register(message: Message, state: FSMContext) -> None:
    if await user_exists(message.from_user.id):
        await message.answer(f"Вы уже зарегистрированы.", reply_markup=menu_keyboard)
    else:
        await message.answer(f"Введите свой никнейм в игре.")
        await state.set_state(Register.nickname)

@router.message(F.text == "Мой статус")
async def status(message: Message) -> None:
    if await user_exists(message.from_user.id):
        user = await get_user(message.from_user.id)
        await message.answer(f"Ваш никнейм: {html.bold(user.nickname)}\n" +
                             f"Статус: {html.bold("Оплачен" if user.paid else "Неоплачен")}",
                             reply_markup=withdraw_keyboard)
    else:
        await message.answer("Вы еще не зарегистрированы.\n" +
                             "Для регистрации нажмите на кнопку ниже.",
                             reply_markup=menu_keyboard)

@router.message(F.text, Register.nickname)
async def set_nickname(message: Message, state: FSMContext) -> None:
    await state.update_data(nickname=message.text)
    data = await state.get_data()
    nickname: str = data.get("nickname").strip()
    
    if await nickname_exists(nickname):
        await message.answer(f"Никнейм {nickname} занят.\nВведите другой никнейм.")
    else:    
        await create_user(message.from_user.id, nickname)            
        await message.answer(f"Вы успешно зарегистрированы с ником {html.bold(nickname)}.")
        await state.clear()

@router.callback_query(F.data == "withdraw")
async def withdraw(callback: CallbackQuery) -> None:
    await delete_user(callback.from_user.id)
    await callback.message.delete()
    await callback.message.answer("Вы были сняты с турнира.", reply_markup=menu_keyboard)