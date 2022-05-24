from aiogram.dispatcher.filters.state import StatesGroup, State


class FlashlightCreate(StatesGroup):
    get_name = State()
    commit = State()
