# @Author Jose Daniel Acuna
# Last time edited 11/1/19
# Reference https://www.journaldev.com/16016/python-parse-json-dumps-loads

import json


# Class for Json encoding
class Game:

    def __init__(self, type, status, piano, targets, cobWeb, balloons):
        self.type = type
        self.status = status
        self.piano = piano
        self.targets = targets
        self.cobWeb = cobWeb
        self.balloons = balloons

    def dict(self):
        return {
            'type': self.type,
            'status': self.status,
            'piano': self.piano,
            'targets': self.targets,
            'cobWeb': self.cobWeb,
            'balloons': self.balloons}

    def to_json(self):
        return json.dumps(self.dict())

