from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default.dictionary import Dictionary

add_remove_sensor_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=Dictionary.add_sensor),
        ],
        [
            KeyboardButton(text=Dictionary.remove_sensor),
        ],
        [
            KeyboardButton(text=Dictionary.remove_room),
        ],
    ],
    resize_keyboard=True,
)
