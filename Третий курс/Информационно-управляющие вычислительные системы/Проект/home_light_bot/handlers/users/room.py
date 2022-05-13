import aiohttp
from aiogram import types
from aiogram.types import InlineKeyboardMarkup

from data.config import IP
from filters.room import IsRoom
from loader import dp
from utils.create_inline_keyboard import RoomInlineKeyBoard


@dp.message_handler(IsRoom())
async def get_rooms(message: types.Message):

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
        url = f'{IP}/api/flash'
        async with session.get(
                url,
                headers={'content-type': 'application/json'},
        ) as resp:
            data = await resp.json()
            keyboard = await RoomInlineKeyBoard(data).get_inline()

    await message.answer(f"Идет поиск по комнатам...")
    if len(data) == 0:
        await message.answer(f"У вас нет ни одной комнаты")
    else:
        inline_keyboard = InlineKeyboardMarkup(
            row_width=1,
            inline_keyboard=keyboard,
        )

        await message.answer(f"Найденные комнаты:",
                             reply_markup=inline_keyboard)
