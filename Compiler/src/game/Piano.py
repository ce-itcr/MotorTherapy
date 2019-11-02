import json


# Class for Json encoding
class Piano:

    def __init__(self, colors, points, time):
        self.colors = colors
        self.points = points
        self.time = time

    def dict(self):
        return {
            'colors': self.colors,
            'points': self.points,
            'time': self.time}

    def to_json(self):
        return json.dumps(self.dict())
