from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp(), state='*')
async def bot_help(message: types.Message, state: FSMContext):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку")

    await state.reset_state()

    await message.answer("\n".join(text))
