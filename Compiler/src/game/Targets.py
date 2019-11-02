# Class for Json encoding
class Targets:

    def __init__(self, x, y, time):
        self.x = x
        self.y = y
        self.time = time

    def dict(self):
        return {
            'x': self.x,
            'y': self.y,
            'time': self.time}
