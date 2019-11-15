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

from src.lexical.Lexical import *
# import src.syntax.Syntax as syn
import src.syntax.Syntax as stx
from src.syntax.Statements import *

def search_in_text(filename, word1, word2):
    f = open(filename, "r")
    str_ret = ""
    index1 = 0
    index2 = 0
    index = False
    for i, line in enumerate(f):
        if line == word1:
            index1 = i
            index = True
        elif line == word2 and index:
            index2 = i
            index = False
    f.close()
    f = open(filename, "r")
    for i, line in enumerate(f):
        if i in range(index1+2, index2):
            str_ret += line
    return str_ret

# def create_archives():
#     game1 = open("game1.txt", "w+")
#     game2 = open("game2.txt", "w+")
#     game3 = open("game3.txt", "w+")
#     game4 = open("game4.txt", "w+")
#     games_array = {0:game1, 1:game2, 2:game3, 3:game4}
#     for i in range(4):
#         games_array[i].write(search_in_text("game.txt", "Game"+str(i+1)+"\n", "}\n"))
#         games_array[i].close()

def extract_variables():
    games_array = []
    for i in range(3):
        data = search_in_text("game.txt", "Game"+str(i+1)+"\n", "}\n")
        # print("lex: " + str(consume(data)))
        stx.parser.parse(data)
        if not stx.compilation_successful:
            exit(1)
        games_array.append(stx.variables)
        stx.variables = {}
    return games_array

games = extract_variables()
print("Game1: " + str(games[0]))
print("Game2: " + str(games[1]))
print("Game3: " + str(games[2]))
