from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils.callback_data import CallbackData

sensor_detail_callback = CallbackData("sensor-detail", "id", "name")
sensor_create_callback = CallbackData("sensor-create")

class SensorCreate(StatesGroup):
    get_name = State()
    commit = State()


class SensorDetail(StatesGroup):
    view_sensor = State()
