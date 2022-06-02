from aiogram.types import InlineKeyboardButton

from models.flashlight import flashlight_create_callback

create_flashlight_inline = [
    InlineKeyboardButton(
        text="Добавить лампочку",
        callback_data=flashlight_create_callback.new()
    )
]
