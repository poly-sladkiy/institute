from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.room import room_detail_callback, create_room


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
        self.keys.append(create_room)

        inline_keyboard = InlineKeyboardMarkup(
            row_width=2,
            inline_keyboard=self.keys,
        )

        return inline_keyboard
