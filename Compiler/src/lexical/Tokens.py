# @Author Jose Daniel Acuna
# Last time edited 10/12/19


# List of keywords
reserved = {
    # LOOPS
    'Begin': 'BEGIN',
    'End': 'END',
    'DO': 'DO',
    'Dow': 'DOW',
    'Enddo': 'ENDDO',
    'FOR': 'FOR',
    'FOREND': 'FOREND',
    'times': 'TIMES',
    'using': 'USING',

    # GAME
    'Main': 'MAIN',
    'Game1': 'GAME1',
    'Game2': 'GAME2',
    'Game3': 'GAME3',
    'Game4': 'GAME4',

    # TYPES
    'int': 'INT',
    'string': 'STRING',
}

# List of token names
tokens = [
    # SYMBOLS
    'ID',
    'SEMCOL',
    'COMMA',
    'NUMBER',

    # OPERATORS
    'EQUAL',
    'PLUS',
    'MINUS',
    'MULTI',
    'DIVIDE',

    # CONTAINERS () [] {}
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LSPAREN',
    'RSPAREN',

] + list(reserved.values())
