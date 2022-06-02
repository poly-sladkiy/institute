from aiogram.types import InlineKeyboardButton

from states.sensor import sensor_create_callback

create_sensor_inline = [
    InlineKeyboardButton(
        text="Создать сенсор",
        callback_data=sensor_create_callback.new()
    )
]