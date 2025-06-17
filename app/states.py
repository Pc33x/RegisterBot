from aiogram.fsm.state import State, StatesGroup

class Register(StatesGroup):
    nickname = State()


class Admin(StatesGroup):
    menu = State()
    set_status = State()