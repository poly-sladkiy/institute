from aiogram.dispatcher.filters.state import StatesGroup, State


class RoomCreate(StatesGroup):
    get_name = State()
    commit = State()


class RoomDetail(StatesGroup):
    view_room = State()
    add_sensor = State()
    remove_sensor = State()
