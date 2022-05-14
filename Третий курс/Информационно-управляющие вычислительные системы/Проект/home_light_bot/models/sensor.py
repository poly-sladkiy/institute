import aiohttp

from data.config import IP


class Sensor:
    def __init__(self, item_id, name, room_id):
        self.id = item_id if item_id is not None else None
        self.name = name if name is not None else None
        self.room_id = room_id if room_id is not None else None

    async def get_all(self):
        session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False))
        url = f'{IP}/api/sensor'
        resp = await session.get(
            url,
            headers={'content-type': 'application/json'})
        data = await resp.json()

        return data

    async def get_detail(self, item_id: int = None):
        if item_id is None:
            return

        session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False))
        url = f'{IP}/api/sensor/{item_id}'
        resp = await session.get(
            url,
            headers={'content-type': 'application/json'})
        data = await resp.json()

        return data

    async def create_item(self, new_sensor: 'Sensor'):
        session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False))
        url = f'{IP}/api/sensor'
        resp = await session.post(
            url,
            json={'name': f'{new_sensor.name}'},
            headers={'content-type': 'application/json'})
        data = await resp.json()

        return data

    async def delete_item(self, item_id: None):
        session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False))
        url = f'{IP}/api/sensor/{item_id}'
        resp = await session.delete(
            url,
            headers={'content-type': 'application/json'})
        data = await resp.json()

        return data
