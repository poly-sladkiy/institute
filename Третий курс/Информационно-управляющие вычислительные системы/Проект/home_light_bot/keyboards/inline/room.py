from aiogram.types import InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

room_detail_callback = CallbackData("room-detail", "id", "name")
room_create_callback = CallbackData("room-create")


create_room = [
    InlineKeyboardButton(
        text="Создать комнату",
        callback_data=room_create_callback.new()
    )
]
