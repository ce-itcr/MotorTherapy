from src.lexical.Lexical import *
import os


def game_test():
    print("\nGame_TEST running...")
    consume(read_file())
    print("OK")


# Reads the game.txt file
def read_file():
    # Open the file
    cur_path = os.path.dirname(__file__)
    path = os.path.relpath('game.txt', cur_path)
    file = open(path, "r")
    print("\tOpen file:", file.name)

    # Read the file
    line = file.read()

    # Close the file
    file.close()

    return line
