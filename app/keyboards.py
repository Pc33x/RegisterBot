from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="📋 Зарегистрироваться")],
              [KeyboardButton(text="📊 Мой профиль")]],
    input_field_placeholder="Нажмите для ниже для продолжения.",
    resize_keyboard=True,
)

withdraw_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Сняться с турнира", callback_data="withdraw")]
    ]
)

admin_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="👥 Список участников")],
              [KeyboardButton(text="🔄 Поменять статус")],
              [KeyboardButton(text="/start")]],
    input_field_placeholder="Нажмите для ниже для продолжения.",
    resize_keyboard=True,
)