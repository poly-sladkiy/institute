from aiogram.dispatcher.filters.state import StatesGroup, State


class SensorCreate(StatesGroup):
    get_name = State()
    commit = State()
