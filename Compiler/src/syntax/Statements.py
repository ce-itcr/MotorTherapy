from src.syntax.Syntax import *
from src.lexical.Tokens import *

def p_statements(p):
    '''
    statements : var_assign statements
               | empty
    '''
    print(p)