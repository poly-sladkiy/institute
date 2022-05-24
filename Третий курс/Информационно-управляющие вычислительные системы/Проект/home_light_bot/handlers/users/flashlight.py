from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from filters.room import IsFlashlight
from keyboards.default.dictionary import Dictionary
from keyboards.default.menu import yes_no_keyboard, menu_keyboard
from keyboards.inline.flashlight import create_flashlight_inline
from keyboards.inline.sensor import create_sensor_inline
from loader import dp
from models.flashlight import flashlight_create_callback, Flashlight, flashlight_detail_callback
from models.sensor import Sensor, sensor_detail_callback, sensor_create_callback
from states.flashlight import FlashlightCreate
from states.sensor import SensorCreate


@dp.message_handler(IsFlashlight())
async def get_flashlight(message: types.Message):
    await message.answer(f"Идет поиск по лампочкам...")

    keys = []
    flashlights = await Flashlight.get_all()
    for flash in flashlights:
        keys.append([
            InlineKeyboardButton(
                text=f"{flash['name']}",
                callback_data=flashlight_detail_callback.new(
                    id=flash['id'],
                    name=flash['name'])
            )
        ])

    keys.append(create_flashlight_inline)
    keyboard = InlineKeyboardMarkup(
        row_width=1,
        inline_keyboard=keys,
    )

    await message.answer(f"Найденные лампочки:",
                         reply_markup=keyboard)


@dp.callback_query_handler(flashlight_create_callback.filter(), state='*')
async def create_flashlight(call: CallbackQuery, callback_data: dict, state: FSMContext):
    await call.message.answer(f"Введите название лампочки",
                              reply_markup=ReplyKeyboardRemove())
    await FlashlightCreate.first()


@dp.message_handler(state=FlashlightCreate.get_name)
async def get_flashlight_name(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(sensor_name=answer)
    await FlashlightCreate.next()

    await message.answer(f"Данные верны: {answer}?",
                         reply_markup=yes_no_keyboard)


@dp.message_handler(state=FlashlightCreate.commit)
async def commit_flashlight_name(message: types.Message, state: FSMContext):
    answer = message.text
    if answer.lower() == Dictionary.no.lower():
        await message.answer(f"Введите название лампочки снова",
                             reply_markup=ReplyKeyboardRemove())
        await FlashlightCreate.get_name.set()
        return
    elif answer.lower() == Dictionary.yes.lower():
        user_data = await state.get_data()

        await message.answer(f"Добавляем новую лампочку...")

        flash = Flashlight(name=f"{user_data.get('sensor_name')}")
        await Flashlight.create_item(flash)

        await message.answer(f"Лампочка успешно добавлен...",
                             reply_markup=menu_keyboard)

        await state.reset_state(with_data=True)
    else:
        await message.answer(f"Вы ввели не корректные данные, попробуйте снова")
