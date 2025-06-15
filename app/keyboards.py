from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

registerKeyboard = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Зарегистрироваться")]],
    input_field_placeholder="Нажмите для ниже для регистрации.",
    resize_keyboard=True,
)