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

def extract_variables():
    games_array = []
    for i in range(0,4):
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
