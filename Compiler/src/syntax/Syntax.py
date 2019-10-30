import ply.yacc as yacc
from src.lexical.Tokens import *
import numpy

variables = {}


def p_For(p):
    '''
    For : FOR NUMBER TIMES USING NUMBER
    '''
    if isinstance(p[5], int):
        return True
    elif isinstance(p[5], list):
        return True

def p_Dow(p):
    '''
    Dow : DOW '(' ID ')'
        | DOW '(' NUMBER ')'
    '''
    if isinstance(p[3], int):
        False
    else:
        for i in range(variables[p[3]]):
            False


def p_var(p):
    '''var : '''

def p_var_assign(p):
    '''
    var_assign : INT ID EQUAL NUMBER SEMCOL
    '''
    if p[2] == '\=':
        variables[p[1]] = p[3]
    elif p[2] == '(':
        variables[p[5]] = numpy.zeros(p[7], int)
    elif p[3] == '[':
        variables[p[2]] = numpy.zeros(p[4], int)
    elif p[1] == 'int':
        variables[p[2]] = p[4]
        print(('=', p[2], p[4]))
        p[0] = ('=', p[2], p[4])

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None


# def p_optitem(p):
#     '''
#     optitem : item'
#             | empty
#     '''
#    if:
#    else:
#        pass

# def p_error(t):
#     if not t:
#         print("puto")
#         return
#     print("Syntax error at '%s'" % t.value)

parser = yacc.yacc()