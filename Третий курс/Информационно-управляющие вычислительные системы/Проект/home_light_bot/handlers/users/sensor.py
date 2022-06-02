from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from filters.room import IsSensor
from keyboards.default.dictionary import Dictionary
from keyboards.default.menu import yes_no_keyboard, menu_keyboard
from keyboards.inline.sensor import create_sensor_inline
from loader import dp
from models.sensor import Sensor
from states.sensor import SensorCreate, sensor_detail_callback, sensor_create_callback


@dp.message_handler(IsSensor())
async def get_sensors(message: types.Message):
    await message.answer(f"Идет поиск по сенсорам...")

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

    keys.append(create_sensor_inline)
    keyboard = InlineKeyboardMarkup(
        row_width=1,
        inline_keyboard=keys,
    )

    await message.answer(f"Найденные сенсоры:",
                         reply_markup=keyboard)


@dp.callback_query_handler(sensor_create_callback.filter(), state='*')
async def create_sensor(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.message.answer(f"Введите название сенсора",
                              reply_markup=ReplyKeyboardRemove())
    await SensorCreate.first()


@dp.callback_query_handler(sensor_detail_callback.filter(), state='*')
async def detail_sensor(call: CallbackQuery, callback_data: dict, state: FSMContext):
    pass

@dp.message_handler(state=SensorCreate.get_name)
async def get_sensor_name(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(sensor_name=answer)
    await SensorCreate.next()

    await message.answer(f"Данные верны: {answer}?",
                         reply_markup=yes_no_keyboard)


@dp.message_handler(state=SensorCreate.commit)
async def commit_sensor_name(message: types.Message, state: FSMContext):
    answer = message.text
    if answer.lower() == Dictionary.no.lower():
        await message.answer(f"Введите название сенсора снова",
                             reply_markup=ReplyKeyboardRemove())
        await SensorCreate.get_name.set()
        return
    elif answer.lower() == Dictionary.yes.lower():
        user_data = await state.get_data()

        await message.answer(f"Добавляем новый сенсор...")

        sensor = Sensor(name=f"{user_data.get('sensor_name')}")
        await Sensor.create_item(sensor)

        await message.answer(f"Сенсор успешно добавлен...",
                             reply_markup=menu_keyboard)

        await state.reset_state(with_data=True)
    else:
        await message.answer(f"Вы ввели не корректные данные, попробуйте снова")
