# @Author Jose Daniel Acuna
# Last time edited 10/12/19

import ply.lex as lex
from src.lexical.Tokens import *
from src.lexical.Rules import *
from src.lexical.Errors import *


# Build the lexer
lexer = lex.lex()


# Function that consumes data
def consume(data):
    lexer.input(data)
    l_tok = []

    # Tokenize the data
    while True:
        tok = lexer.token()
        if not tok:
            break
        l_tok.append(tok)

    return l_tok


# Function that loops the tokens
def printTokens(l_tokens):
    print("LexToken(type, value, line, pos)")
    for tok in l_tokens:
        print(tok)
