from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from filters.room import IsSensor
from keyboards.default.menu import yes_no_keyboard
from keyboards.inline.sensor import create_sensor
from loader import dp
from models.sensor import Sensor, sensor_detail_callback, sensor_create_callback
from states.room import Create


@dp.message_handler(IsSensor())
async def get_sensors(message: types.Message):
    await message.answer(f"Идет поиск по сенсорам...",
                         reply_markup=ReplyKeyboardRemove())

    keys = []
    sensors = await Sensor.get_all()
    for sensor in sensors:
        keys.append([
            InlineKeyboardButton(
                text=f"{sensor['name']}",
                callback_data=sensor_detail_callback.new(
                    id=sensor['id'],
                    name=sensor['name'])
            )
        ])

    keys.append(create_sensor)
    keyboard = InlineKeyboardMarkup(
        row_width=1,
        inline_keyboard=keys,
    )

    await message.answer(f"Найденные сенсоры:",
                         reply_markup=keyboard)


@dp.callback_query_handler(sensor_create_callback.filter(), state='*')
async def create_sensor(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.message.answer(f"Введите название комнаты")
    await Create.first()


# todo: create states for create sensor
@dp.message_handler(state=Create.get_name)
async def get_sensor_name(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(room_name=answer)
    await Create.next()

    await message.answer(f"Данные верны: {answer}?",
                         reply_markup=yes_no_keyboard)
