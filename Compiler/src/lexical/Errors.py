# @Author Jose Daniel Acuna
# Last time edited 10/16/19


# Error handling for invalid characters
def t_error(t):
    line = read_line(t.value)
    error = "Lexical error: {0} in line {1}".format(line, t.lineno)
    print(error)
    exit(1)


# Read a string an slits it when find '\n'
def read_line(s):
    s2 = s.split("\n")[0]
    return s2
