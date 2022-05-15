import aiohttp
from aiogram.utils.callback_data import CallbackData

from data.config import IP

flashlight_detail_callback = CallbackData("flash-detail", "id", "name")
flashlight_create_callback = CallbackData("flash-create")


class Flashlight:
    def __init__(self, item_id=None, name=None, room_id=None):
        self.id = item_id if item_id is not None else None
        self.name = name if name is not None else None
        self.sensor_id = room_id if room_id is not None else None

    @staticmethod
    async def get_all():
        session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False))
        url = f'{IP}/api/flash'
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
        url = f'{IP}/api/flash/{item_id}'
        resp = await session.get(
            url,
            headers={'content-type': 'application/json'})
        data = await resp.json()
        await session.close()

        return data

    @staticmethod
    async def create_item(new_sensor: 'Flashlight'):
        session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False))
        url = f'{IP}/api/flash'
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
        url = f'{IP}/api/flash/{item_id}'
        resp = await session.delete(
            url,
            headers={'content-type': 'application/json'})
        data = await resp.json()
        await session.close()

        return data
