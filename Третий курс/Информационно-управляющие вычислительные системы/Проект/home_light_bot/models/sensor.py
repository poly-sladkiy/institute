import aiohttp
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.callback_data import CallbackData

from data.config import IP
from states.room import add_sensor_callback, remove_sensor_callback




class Sensor:
    def __init__(self, item_id=None, name=None, room_id=None):
        self.id = item_id if item_id is not None else None
        self.name = name if name is not None else None
        self.room_id = room_id if room_id is not None else None

    def __str__(self):
        return self.name

    @staticmethod
    async def get_all():
        session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False))
        url = f'{IP}/api/sensor'
        resp = await session.get(
            url,
            headers={'content-type': 'application/json'})
        data = await resp.json()

        await session.close()

        return data

    @staticmethod
    async def get_detail(item_id: int = None):
        if item_id is None:
            return

        session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False))
        url = f'{IP}/api/sensor/{item_id}'
        resp = await session.get(
            url,
            headers={'content-type': 'application/json'})
        data = await resp.json()
        await session.close()

        return data

    @staticmethod
    async def get_free(inline: bool = False, room_id: int = None):
        session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False))
        url = f'{IP}/api/sensors/free/'
        resp = await session.get(
            url,
            headers={'content-type': 'application/json'})
        data = await resp.json()
        await session.close()

        if not inline:
            sensors = []
            for i in data:
                _sensor = Sensor(item_id=i.get("id"), name=i.get("name"))
                sensors.append(_sensor)
            return sensors

        else:
            keys = []
            for i in data:
                keys.append([
                    InlineKeyboardButton(
                        text=f"{i.get('name')}",
                        callback_data=add_sensor_callback.new(
                            sensor_id=i.get('id'),
                            room_id=room_id,
                            name=i.get('name')),
                    )
                ])

            keyboard = InlineKeyboardMarkup(
                row_width=1,
                inline_keyboard=keys,
            )
            return keyboard, len(keys)

    @staticmethod
    async def create_item(new_sensor: 'Sensor'):
        session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False))
        url = f'{IP}/api/sensor'
        resp = await session.post(
            url,
            json={'name': f'{new_sensor.name}'},
            headers={'content-type': 'application/json'})
        data = await resp.json()
        await session.close()

        return data

    @staticmethod
    async def get_room_for_delete(room_id: int = None):
        session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False))
        url = f'{IP}/api/room/{room_id}'
        resp = await session.get(
            url,
            headers={'content-type': 'application/json'})
        data = await resp.json()
        sensors = data.get('sensors')
        await session.close()

        keys = []
        for i in sensors:
            keys.append([
                    InlineKeyboardButton(
                        text=f"{i.get('name')}",
                        callback_data=remove_sensor_callback.new(
                            sensor_id=i.get('id'),
                            room_id=room_id,
                            name=i.get('name')),
                    )
                ])

        keyboard = InlineKeyboardMarkup(
            row_width=1,
            inline_keyboard=keys,
        )

        return keyboard, len(keys)

    @staticmethod
    async def delete_item(item_id: None):
        session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False))
        url = f'{IP}/api/sensor/{item_id}'
        resp = await session.delete(
            url,
            headers={'content-type': 'application/json'})
        data = await resp.json()
        await session.close()

        return data
