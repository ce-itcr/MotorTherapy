from game.Balloons import Balloons
from game.CobWeb import CobWeb, Card
from game.Game import Game
from game.Piano import Piano
from game.Targets import Targets


piano = Piano(["red", "blue", "green", "yellow"],
              [1, 2, 3, 4],
              60).dict()

targets = Targets(5, 6, 30).dict()

balloons = Balloons(5, 6).dict()

cobWeb = CobWeb([Card("ocean", 10, 0, 0).dict(),
                 Card("sky", 5, 0, 1).dict(),
                 Card("river", 4, 1, 0).dict(),
                 Card("mountain", 8, 1, 1).dict()
                 ]).dict()

game = Game("", "", piano, targets, cobWeb, balloons)

print(game.to_json())
