import aiohttp

from data.config import IP


class Room:
    def __init__(self, data: dict = None):
        self.id = data.get('id')
        self.name = data.get('name')
        self.sensors = []  # todo: convert to sensors types

    def __str__(self):
        return f"Комната: {self.name}"

    def get_sensors(self):
        return self.sensors

    @staticmethod
    async def get_detail(item_id: int = None):
        if item_id is None:
            return

        session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False))
        url = f'{IP}/api/room/{item_id}'
        resp = await session.get(
            url,
            headers={'content-type': 'application/json'})
        data = await resp.json()
        await session.close()

        room = Room(data)

        return room

    @staticmethod
    async def remove_room(item_id: int = None):
        if item_id is None:
            return False

        session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False))
        url = f'{IP}/api/room/{item_id}'
        resp = await session.delete(
            url,
            headers={'content-type': 'application/json'})
        data = await resp.json()
        await session.close()

        return data.get('state')
