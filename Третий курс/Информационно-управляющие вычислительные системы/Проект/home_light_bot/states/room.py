from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils.callback_data import CallbackData

add_sensor_callback = CallbackData("add-sensor", "sensor_id", "room_id", "name")
remove_sensor_callback = CallbackData("add-sensor", "sensor_id", "room_id", "name")


class RoomCreate(StatesGroup):
    get_name = State()
    commit = State()


class RoomDetail(StatesGroup):
    view_room = State()
    add_sensor = State()
    remove_sensor = State()
