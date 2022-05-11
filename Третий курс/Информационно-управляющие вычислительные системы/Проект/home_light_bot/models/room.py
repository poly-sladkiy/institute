class Room:
    def __init__(self, data: dict = None):
        self.id = data.get('id')
        self.name = data.get('name')
        self.sensors = []  # todo: convert to sensors types

    def __str__(self):
        return f"Комната: {self.name}"

    def get_sensors(self):
        return self.sensors
