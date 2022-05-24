import aiohttp
from aiogram.utils.callback_data import CallbackData

from data.config import IP

sensor_detail_callback = CallbackData("sensor-detail", "id", "name")
sensor_create_callback = CallbackData("sensor-create")


class Sensor:
    def __init__(self, item_id=None, name=None, room_id=None):
        self.id = item_id if item_id is not None else None
        self.name = name if name is not None else None
        self.room_id = room_id if room_id is not None else None

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
    async def delete_item(item_id: None):
        session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False))
        url = f'{IP}/api/sensor/{item_id}'
        resp = await session.delete(
            url,
            headers={'content-type': 'application/json'})
        data = await resp.json()
        await session.close()

        return data
