from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default.dictionary import Dictionary

remove_sensor_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=Dictionary.remove_sensor),
        ],
    ],
    resize_keyboard=True,
)