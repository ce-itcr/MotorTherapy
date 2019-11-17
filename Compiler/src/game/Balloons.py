import json


# Class for Json encoding
class Balloons:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dict(self):
        return {
            'x': self.x,
            'y': self.y}

    def to_json(self):
        return json.dumps(self.dict())
