# @Author Jose Daniel Acuna
# Last time edited 10/12/19
import numpy
import ply.lex as lex
import ply.yacc as yacc
import src.syntax.Syntax as stx
from src.lexical.Tokens import *
from src.lexical.Rules import *
from src.lexical.Errors import *

variables = {}

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
    # print(l_tok)
    return l_tok


# Function that loops the tokens
def printTokens(l_tokens):
    print("LexToken(type, value, line, pos)")
    for tok in l_tokens:
        print(tok)

# def p_For(p):
#     '''
#     For : FOR NUMBER TIMES USING NUMBER
#     '''
#     if isinstance(p[5], int):
#         return True
#     elif isinstance(p[5], list):
#         return True
#
# def p_Dow(p):
#     '''
#     Dow : DOW '(' ID ')'
#         | DOW '(' NUMBER ')'
#     '''
#     if isinstance(p[3], int):
#         False
#     else:
#         for i in range(variables[p[3]]):
#             False
#
#
# def p_var(p):
#     '''var : '''
#
# def p_var_assign(p):
#     '''var_assign : ID EQUAL NUMBER
#                   | ID EQUAL TEXT
#                   | 'i' 'n' 't' ID EQUAL NUMBER
#                   | 's' 't' 'r' 'i' 'n' 'g' '(' NUMBER ')' ID '[' NUMBER ']'
#                   | 'i' 'n' 't' ID '[' NUMBER ']'
#     '''
#     if p[2] == '\=':
#         variables[p[1]] = p[3]
#     elif p[2] == '(':
#         variables[p[5]] = numpy.zeros(p[7], int)
#     elif p[3] == '[':
#         variables[p[2]] = numpy.zeros(p[4], int)
#
# def p_empty(p):
#     '''
#     empty :
#     '''
#     p[0] = None
#
#
# # def p_optitem(p):
# #     '''
# #     optitem : item'
# #             | empty
# #     '''
# #    if:
# #    else:
# #        pass
#
# # def p_error(p):
# #     print("Syntax error at line " + p.lineno(0))
#
# parser = yacc.yacc()