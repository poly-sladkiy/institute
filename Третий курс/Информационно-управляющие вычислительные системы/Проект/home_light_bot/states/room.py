from aiogram.dispatcher.filters.state import StatesGroup, State


class RoomCreate(StatesGroup):
    get_name = State()
    commit = State()
