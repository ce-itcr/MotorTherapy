from server.Server import *
from game.GameController import GameController
from Compiler import compile
from game.GameDataBase import GamesDB


# Example of the program
def main():
    # Compiles and gets the games tables from compiler
    games = compile("../game.txt")
    games_db = GamesDB(games)

    # Runs the Code of the Game and handle the loops
    game_controller = GameController(games_db)

    # Calls for update() whenever the Server receives a message
    ClientObserver.observers.append(game_controller)

    # Puts the Server on listening mode
    Server().start()


main()
