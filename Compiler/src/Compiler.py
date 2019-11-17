from src.lexical.Lexical import *
from src.syntax.Statements import *
import src.syntax.Syntax as stx


# Search for the word in the file
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
        if i in range(index1 + 2, index2):
            str_ret += line
    return str_ret


# Calls the compiler and returns the games tables
def extract_variables(filename):
    games_array = []
    for i in range(4):
        data = search_in_text(filename, "Game" + str(i + 1) + "\n", "}\n")
        stx.parser.parse(data)
        if not stx.compilation_successful:
            exit(1)
        games_array.append(stx.variables)
        stx.variables = {}
    return games_array


def compile(filename):
    print("Compiling: %s" % filename)
    return extract_variables(filename)
