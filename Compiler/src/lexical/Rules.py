# @Author Jose Daniel Acuna
# Last time edited 10/12/19

from src.lexical.Tokens import reserved


# Regular expressions for simple tokens
t_EQUAL = r'\='
t_COMMA = r'\,'
t_SEMCOL = r'\;'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTI = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LSPAREN = r'\['
t_RSPAREN = r'\]'


# Rule to define identifiers
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


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