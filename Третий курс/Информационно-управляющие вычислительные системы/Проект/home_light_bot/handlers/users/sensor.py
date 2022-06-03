from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from filters.room import IsSensor
from keyboards.default.dictionary import Dictionary
from keyboards.default.menu import yes_no_keyboard, menu_keyboard
from keyboards.default.sensor import remove_sensor_keyboard
from keyboards.inline.sensor import create_sensor_inline
from loader import dp
import models.sensor
from states.sensor import SensorCreate, sensor_detail_callback, sensor_create_callback, SensorDetail


@dp.message_handler(IsSensor())
async def get_sensors(message: types.Message):
    await message.answer(f"Идет поиск по сенсорам...")

    keys = []
    sensors = await models.sensor.Sensor.get_all()
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


@dp.callback_query_handler(sensor_detail_callback.filter(), state='*')
async def detail_sensor(call: CallbackQuery, callback_data: dict, state: FSMContext):
    sensor_id = callback_data.get("id")
    sensor = await models.sensor.Sensor.get_detail(sensor_id)

    await SensorDetail.first()
    await state.update_data(sensor_id=sensor_id)

    await call.message.answer(f"<code>Сенсор {sensor.name}</code>\n\n"
                              f"Идентификатор: {sensor.id}\n"
                              f"Название: {sensor.name}\n"
                              f"Комната: {sensor.room.name if sensor.room is not None else 'не устновлена'}",
                              reply_markup=remove_sensor_keyboard
                              )


@dp.message_handler(state=SensorDetail.view_sensor)
async def commit_sensor_name(message: types.Message, state: FSMContext):
    answer = message.text.lower()
    data = await state.get_data()

    if answer == Dictionary.remove_sensor.lower():
        await message.answer(f"Идет удаление сенсора")
        await models.sensor.Sensor.delete_item(data.get("sensor_id"))
        await message.answer(f"Сенсор успешно удален",
                             reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer(f"Не верный формат ответа")

    await state.reset_state(with_data=True)


@dp.callback_query_handler(sensor_create_callback.filter(), state='*')
async def create_sensor(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.message.answer(f"Введите название сенсора",
                              reply_markup=ReplyKeyboardRemove())
    await SensorCreate.first()


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

        sensor = models.sensor.Sensor(name=f"{user_data.get('sensor_name')}")
        await models.sensor.Sensor.create_item(sensor)

        await message.answer(f"Сенсор успешно добавлен...",
                             reply_markup=menu_keyboard)

        await state.reset_state(with_data=True)
    else:
        await message.answer(f"Вы ввели не корректные данные, попробуйте снова")
