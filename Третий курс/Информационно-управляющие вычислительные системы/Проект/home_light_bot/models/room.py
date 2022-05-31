import aiohttp
from aiogram.utils.callback_data import CallbackData

from data.config import IP
from models.sensor import Sensor


class Room:
    def __init__(self, data: dict = None):
        self.id = data.get('id')
        self.name = data.get('name')

        self.sensors = []

        if len(data.get('sensors')) < 0:
            self.sensors = []  # todo: convert to sensors types
        else:
            for i in data.get('sensors'):
                self.sensors.append(Sensor(item_id=i.get('id'), name=i.get('name')))

    def __str__(self):
        return f"Комната: {self.name}"

    def get_sensors(self):
        answer = []
        for sensor in self.sensors:
            answer.append(str(sensor))
        return str(answer)

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

    @staticmethod
    async def add_sensor(room_id: int = None, sensor_id: int = None):
        session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False))
        url = f'{IP}/api/room/add-sensor?roomId={room_id}&sensorId={sensor_id}'
        await session.put(
            url,
            headers={'content-type': 'application/json'})
        await session.close()

    @staticmethod
    async def remove_sensor(room_id: int = None, sensor_id: int = None):
        session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False))
        url = f'{IP}/api/room/remove-sensor?roomId={room_id}&sensorId={sensor_id}'
        await session.put(
            url,
            headers={'content-type': 'application/json'})
        await session.close()
