# @Author Jose Daniel Acuna
# Last time edited 10/12/19


# Error handling for invalid characters
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
