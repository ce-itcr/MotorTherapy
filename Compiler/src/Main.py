from server.Server import *
from game.GameController import GameController
from Compiler import compile
from game.GameDataBase import GamesDB


def extract_variables():
    games_array = []
    for i in range(4):
        data = search_in_text("game.txt", "Game"+str(i+1)+"\n", "}\n")
        # print("lex: " + str(consume(data)))
        print("\n\nGame {0}".format(i+1))
        print("-------------------------------------------------------------")
        stx.parser.parse(data)
        if not stx.compilation_successful:
            games_array = []
            exit(1)
        games_array.append(stx.variables)
        stx.variables = {}
    return games_array

games = extract_variables()
print("\n")
for i in range(4):
    print("Final dictionary for Game{0}: {1}".format(i+1, games[i]))

    # Calls for update() whenever the Server receives a message
    ClientObserver.observers.append(game_controller)

    # Puts the Server on listening mode
    Server().start()


main()
