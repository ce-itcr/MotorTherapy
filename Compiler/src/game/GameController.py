# @Author Jose Daniel Acuna
# Last time edited 11/14/19
from game.Balloons import Balloons
from game.CobWeb import *
from game.Game import Game
from game.Piano import Piano
from game.Targets import Targets
from server.ClientObserver import *


class GameController:

    def __init__(self, games_db):
        self.gamesDB = games_db
        self.piano_i = 0
        self.balloons_i = 0
        self.targets_i = 0
        self.cob_web_i = 0

    def update(self, message):
        game = Game.from_json(message)

        if game.status == "ok":
            response = self.handle_games(game.type)
        else:
            response = GameController.handle_errors()

        ClientObserver.client_response = response

    # Switch statement
    def handle_games(self, game_type):
        switch = 0
        if game_type == "piano":
            switch = self.piano()
        elif game_type == "targets":
            switch = self.targets()
        elif game_type == "balloons":
            switch = self.balloons()
        elif game_type == "cobWeb":
            switch = self.cob_web()

        if switch != 0:
            return switch.to_json()
        else:
            return GameController.handle_end()

    @staticmethod
    def handle_errors():
        return Game(status="error").to_json()

    @staticmethod
    def handle_end():
        return Game(status="end").to_json()

    # Example in case the client is in the piano game
    def piano(self):
        i = self.piano_i
        piano = self.gamesDB.piano[i]

        if i < len(self.gamesDB.piano) - 1:
            self.piano_i += 1
            return Game(type="piano", piano=piano.dict())
        else:
            return 0

    # Example in case the client is in the targets game
    def targets(self):
        return
        i = self.targets_i
        targets = Targets(5, 6, 30)
        #targets = self.gamesDB.targets[i]

        #if i < len(self.gamesDB.targets) - 1: # self.targets_+= 1
        return Game(type="targets", targets=targets.dict())
        #else: return 0

    # Example in case the client is in the balloons game
    def balloons(self):
        i = self.balloons_i
        balloons = self.gamesDB.balloons[i]

        if i < len(self.gamesDB.balloons) - 1:
            self.balloons_i += 1
            return Game(type="balloons", balloons=balloons.dict())
        else:
            return 0

    # Example in case the client is in the cobWeb game
    def cob_web(self):
        i = self.cob_web_i
        cob_web = self.gamesDB.cob_web

        if i < 1:
            self.cob_web_i += 1
            return Game(type="cobWeb", cobWeb=cob_web.dict())
        else:
            return 0
