# @Author Jose Daniel Acuna
# Last time edited 11/1/19
from game.Balloons import Balloons
from game.CobWeb import *
from game.Game import Game
from game.Piano import Piano
from game.Targets import Targets
from server.ClientObserver import *


class GameController:

    @staticmethod
    def update(message):
        game = Game.from_json(message)
        if game.status == "ok":
            ClientObserver.client_response = GameController.handle_games(game.type)
        else:
            GameController.handle_errors()

    # Switch statement
    @staticmethod
    def handle_games(game_type):
        switch = \
            {
                'piano': GameController.piano(),
                'targets': GameController.targets(),
                'balloons': GameController.balloons(),
                'cobWeb': GameController.cob_web()
            }.get(game_type, 0)

        if switch != 0:
            return switch.to_json()
        else:
            return ""

    @staticmethod
    def handle_errors():
        return

    # Example in case the client is in the piano game
    @staticmethod
    def piano():
        piano = Piano(["red", "blue", "green", "yellow"],
                      [1, 2, 3, 4],
                      60).dict()
        return Game(type="piano", piano=piano)

    # Example in case the client is in the targets game
    @staticmethod
    def targets():
        targets = Targets(5, 6, 30).dict()
        return Game(type="targets", targets=targets)

    # Example in case the client is in the balloons game
    @staticmethod
    def balloons():
        balloons = Balloons(5, 6).dict()
        return Game(type="balloons", balloons=balloons)

    # Example in case the client is in the cobWeb game
    @staticmethod
    def cob_web():
        cob_web = CobWeb([Card("ocean", 10, 0, 0).dict(),
                          Card("sky", 5, 0, 1).dict(),
                          Card("river", 4, 1, 0).dict(),
                          Card("mountain", 8, 1, 1).dict()
                          ]).dict()
        return Game(type="cobWeb", cobWeb=cob_web)
