import aiohttp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ReplyKeyboardRemove

from data.config import IP
from filters.room import IsRoom
from keyboards.default.dictionary import Dictionary
from keyboards.default.menu import yes_no_keyboard, menu_keyboard
from keyboards.default.room import add_remove_sensor_keyboard
from keyboards.inline.room import room_create_callback, room_detail_callback
from loader import dp
from models.room import Room
from states.room import RoomCreate
from utils.create_inline_keyboard import RoomInlineKeyBoard


@dp.message_handler(IsRoom())
async def get_rooms(message: types.Message):

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
        url = f'{IP}/api/room'
        async with session.get(
                url,
                headers={'content-type': 'application/json'},
        ) as resp:
            data = await resp.json()
            keyboard = await RoomInlineKeyBoard(data).get_inline()

    await message.answer(f"Идет поиск по комнатам...")
    await message.answer(f"Найденные комнаты:",
                         reply_markup=keyboard)


@dp.callback_query_handler(room_create_callback.filter(), state='*')
async def create_room(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.message.answer(f"Введите название комнаты",
                              reply_markup=ReplyKeyboardRemove())
    await RoomCreate.first()


@dp.callback_query_handler(room_detail_callback.filter(), state='*')
async def create_room(call: CallbackQuery, callback_data: dict, state: FSMContext):

    room = await Room.get_detail(callback_data.get("id"))

    await call.message.answer(f"<code>Комната {room.name}</code>\n"
                              f""
                              f"Идентификатор: {room.id}\n"
                              f"Название: {room.name}\n"
                              f"Сенсоры: {room.sensors if len(room.sensors) > 0 else 'не установлены'}",
                              reply_markup=add_remove_sensor_keyboard)


@dp.message_handler(state=RoomCreate.get_name)
async def get_room_name(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(room_name=answer)
    await RoomCreate.next()

    await message.answer(f"Данные верны: {answer}?",
                         reply_markup=yes_no_keyboard)


@dp.message_handler(state=RoomCreate.commit)
async def commit_room_name(message: types.Message, state: FSMContext):
    answer = message.text
    if answer.lower() == Dictionary.no.lower():
        await message.answer(f"Введите название комнаты снова",
                             reply_markup=ReplyKeyboardRemove())
        await RoomCreate.get_name.set()
        return
    elif answer.lower() == Dictionary.yes.lower():
        user_data = await state.get_data()

        await message.answer(f"Добавляем новую комнату...")

        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
            url = f'{IP}/api/room'
            async with session.post(
                url,
                json={'name': user_data.get('room_name')},
                headers={'content-type': 'application/json'},
            ) as resp:
                pass

        await message.answer(f"Комната успешно добавлена...",
                             reply_markup=menu_keyboard)

        await state.reset_state(with_data=True)
    else:
        await message.answer(f"Вы ввели не корректные данные, попробуйте снова")
