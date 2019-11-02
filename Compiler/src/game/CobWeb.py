import json


# Class for Json encoding
class CobWeb:

    def __init__(self, cards):
        self.cards = cards

    def dict(self):
        return {
            'cards': self.cards}

    def to_json(self):
        return json.dumps(self.dict())


class Card:

    def __init__(self, name, points, i, j):
        self.name = name
        self.points = points
        self.i = i
        self.j = j

    def dict(self):
        return {
            'name': self.name,
            'points': self.points,
            'i': self.i,
            'j': self.j}
