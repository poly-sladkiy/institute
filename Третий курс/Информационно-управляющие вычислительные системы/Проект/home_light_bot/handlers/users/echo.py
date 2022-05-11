from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp


@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message):
    await message.answer(f"Команда не найдена попробуйте снова\n"
                         f"<code>{message.text}</code>")
