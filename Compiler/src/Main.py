from server.Server import *
from game.GameController import GameController


# Example of the program
def main():
    # Runs the Code of the Game and handle the loops
    game_controller = GameController()

    # Calls for update() whenever the Server receives a message
    ClientObserver.observers.append(game_controller)

    Server().start()  # Puts the Server on listening mode


main()
