from aiogram.types import InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

room_detail_callback = CallbackData("room-detail", "id", "name")


class RoomInlineKeyBoard:
    def __init__(self, data: dict):
        self.data = data
        self.keys = []

    async def get_inline(self):
        for i in self.data:
            _key = [
                InlineKeyboardButton(
                    text=f"{i['name']}",
                    callback_data=room_detail_callback.new(
                        id=i['id'],
                        name=i['name'])
                )
            ]
            self.keys.append(_key)

        return self.keys
