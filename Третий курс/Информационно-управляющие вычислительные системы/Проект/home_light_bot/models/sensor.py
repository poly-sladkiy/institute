from models.room import Room


class Sensor:
    def __init__(self, data: dict = None):
        self.id = data.get('id')
        self.name = data.get('name')
        self.data = []  # todo: convert to data types
        self.flashlight = []  # todo: convert to data types
        self.room = Room()

    def __str__(self):
        return f"Сенсор: {self.name}\nЛампочек: {len(self.flashlight)} шт."

    def get_flashlight(self):
        return self.flashlight
