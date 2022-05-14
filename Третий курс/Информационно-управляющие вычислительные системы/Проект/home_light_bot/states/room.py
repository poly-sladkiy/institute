from aiogram.dispatcher.filters.state import StatesGroup, State


class Create(StatesGroup):
    get_name = State()
    commit = State()
