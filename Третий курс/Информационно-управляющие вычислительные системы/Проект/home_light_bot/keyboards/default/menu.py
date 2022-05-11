from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.default.dictionary import Dictionary

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=Dictionary.rooms),
            KeyboardButton(text=Dictionary.sensors),
        ],
        [
            KeyboardButton(text=Dictionary.flash),
        ],
    ],
    resize_keyboard=True,
)
