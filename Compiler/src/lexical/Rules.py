# @Author Jose Daniel Acuna
# Last time edited 10/16/19


# Regular expressions for simple tokens
t_EQUAL = r'\='
t_COMMA = r','
t_SEMCOL = r';'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTI = r'\*'
t_DIVIDE = r'/'

# Containers
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LSPAREN = r'\['
t_RSPAREN = r'\]'

# Loops
t_BEGIN = r'Begin'
t_END = r'End'
t_DO = r'DO'
t_DOW = r'Dow'
t_ENDDO = r'Enddo'
t_FOR = r'FOR'
t_FOREND = r'FOREND'
t_TIMES = r'Times'
t_USING = r'Using'

# Game
t_MAIN = r'Main'
t_GAME = r'Game[1-4]'

# Types
t_INT = r'Int'
t_STRING = r'String'

# Functions
t_BALLOON = 'Balloon'
t_INC = 'Inc'
t_DEC = 'Dec'
t_RANDOM = 'Random'
t_FORASIGNWORD = 'ForAsignWord'
t_ASIGNWORD = 'AsignWord'
t_OBJECT = 'Object'
t_SPIDERWEB = 'SpiderWeb'

# Rule to define identifiers
t_ID = r'[a-z][a-zA-Z0-9_&@-]*'

# Rule for strings
t_TEXT = r'"[a-zA-Z0-9_ ]*"'


# Rule to define a integers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


# Rule to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Rule with characters to ignore
t_ignore = ' \t'
t_ignore_COMMENT = r'//.*'
