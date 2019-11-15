from game.Balloons import Balloons
from game.Piano import Piano
from game.Targets import Targets
from game.CobWeb import CobWeb, Card


class GamesDB:

    def __init__(self, games):
        self.balloons = []
        self.piano = []
        self.cob_web = None
        self.targets = []

        self.create_arrays(games)

    def create_arrays(self, games):
        self.create_balloons(games[0])
        self.create_piano(games[1])
        self.crete_cobweb(games[2])

    def create_balloons(self, dict):
        coords_array = dict["Balloons"]
        for pair in coords_array:
            x = pair[0]
            y = pair[1]
            self.balloons.append(Balloons(x, y))

    def create_piano(self, dict):
        colors_rand = dict["Randomcolor"]
        points = dict["points"][0]
        time = dict["times"]
        size = len(colors_rand)

        for i in range(size):
            colors = GamesDB.strings_normalize(colors_rand[i])
            piano = Piano(colors, points, time[i])
            self.piano.append(piano)

    def crete_cobweb(self, dict):
        rows = dict["rows"][0]
        columns = dict["columns"][0]
        web = dict["spiderWeb"]
        cards = []

        for i in range(rows):
            for j in range(columns):
                card = web[i][j]
                name = GamesDB.string_normalize(card[0])
                points = card[1]

                cards.append(Card(name, points, i, j).dict())

        self.cob_web = CobWeb(cards)

    def create_targets(self, dict):
        pass

    @staticmethod
    def string_normalize(str):
        return str.replace('\"', '')

    @staticmethod
    def strings_normalize(array):
        strings = []
        for str in array:
            normalized = GamesDB.string_normalize(str)
            strings.append(normalized)
        return strings
