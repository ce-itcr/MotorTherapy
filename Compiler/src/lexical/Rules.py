# @Author Jose Daniel Acuna
# Last time edited 10/12/19


# Regular expressions for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTI = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'


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
