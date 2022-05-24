from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from keyboards.default.dictionary import Dictionary


class IsRoom(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.text.lower() == Dictionary.rooms.lower()


class IsSensor(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.text.lower() == Dictionary.sensors.lower()


class IsFlashlight(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.text.lower() == Dictionary.flash.lower()
