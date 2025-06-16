from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Зарегистрироваться")],
              [KeyboardButton(text="Мой статус")]],
    input_field_placeholder="Нажмите для ниже для продолжения.",
    resize_keyboard=True,
)

withdraw_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Сняться с турнира", callback_data="withdraw")]
    ]
) 