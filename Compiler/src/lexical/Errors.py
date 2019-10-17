# @Author Jose Daniel Acuna
# Last time edited 10/12/19


# Error handling for invalid characters
def t_error(t):
    error = "Lexical error: {0} in line {1}".format(t.value[0], t.lineno)
    print(error)
    exit(1)
