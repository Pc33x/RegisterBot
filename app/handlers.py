from aiogram import F, Router, html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.keyboards import registerKeyboard
from app.states import Register

router = Router()

@router.message(CommandStart())
async def start(message: Message) -> None:
    await message.answer(
        f"Здравствуй, дорогой {html.bold(message.from_user.full_name)}!\n" +
        f"\nДобро пожаловать в бота от группы {html.link("Панамера", "https://t.me/panamera221")}.\n" +
        f"Для регистрации на {html.italic("турнир")} просто нажми {html.bold("кнопку")} ниже.",
        reply_markup=registerKeyboard
    )
    
@router.message(F.text == "Зарегистрироваться")
async def register(message: Message, state: FSMContext) -> None:
    await message.answer(f"Введите свой никнейм в игре.")
    await state.set_state(Register.nickname)

@router.message(F.text, Register.nickname)
async def set_nickname(message: Message, state: FSMContext) -> None:
    await state.update_data(nickname=message.text)
    data = await state.get_data()
    nickname: str = data.get("nickname").strip()

    await message.answer(f"Вы успешно зарегистрированы с ником {html.bold(nickname)}.")
    await state.clear()