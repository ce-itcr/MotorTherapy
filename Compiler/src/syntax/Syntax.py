import ply.yacc as yacc
from src.lexical.Tokens import *
from src.syntax.Statements import *
import numpy
import src.syntax.Excecution as ex

variables = {'i':[0, 'Int']}
loop_array = []
start = 'statements'

def p_var_assign(p):
    '''
    var_assign : TYPE ID LSPAREN NUMBER RSPAREN SEMCOL
               | TYPE ID SEMCOL
    '''
    global variables
    if p[3] == '[':
        if p[1][0] == 'Int':

            print(("Created", p[2]))
            variables[p[2]] = [[], p[1][0], p[4]]
        elif p[1][0] == 'String':
            print(("Created", p[2]))
            variables[p[2]] = [[], p[1][0], p[4], p[1][1]] # dato, tipo, tamaño array, tamaño string
    else:
        try:
            print(("Created", p[2]))
            variables[p[2]] = ["", p[1][0], p[1][1]]
        except:
            print(("Created", p[2]))
            variables[p[2]] = [0, p[1][0]]

def p_var_define(p):
    '''
    var_define : ID EQUAL ATOMIC SEMCOL
               | ID LSPAREN NUMBER RSPAREN EQUAL ATOMIC SEMCOL
               | TYPE ID EQUAL ATOMIC SEMCOL
    '''
    global variables
    if p[3] == '=':
        try:
            variables[p[2]] = [p[3], p[1][0], p[1][1]]
        except:
            print(("=", p[2], p[4]))
            variables[p[2]] = [p[3], p[1][0]]
    elif p[2] == '=':
        if variables[p[1]][1] == 'String':
            if isinstance(p[3], str):
                if len(p[3]) <= variables[p[1]][2]:
                    # excecute.change_atomic('String', p[3])
                    variables[p[1]][0] = p[3]
                else:
                    print("Tamaño de String es incompatible en " + p[1])
            else:
                print("Error en la definicion de " + p[1])
        else:
            if isinstance(p[3], int):
                # excecute.change_atomic('Int', p[3])
                print(("=", p[1], p[3]))
                variables[p[1]][0] = p[3]
            else:
                print("Error en la definicion de " + p[1])
    elif p[5] == '=':
        if variables[p[1]][1] == 'String':
            if isinstance(variables[p[1]][0], list):
                if isinstance(p[6], str):
                    if len(p[6]) <= variables[p[1]][3]:
                        if len(variables[p[1]][0]) > p[3]:
                            # excecute.change_atomic('String', p[3])
                            variables[p[1]][0][p[3]] = p[6]
                        elif len(variables[p[1]][0]) == p[3]:
                            variables[p[1]][0].append(p[6])
                        else:
                            print("Indice fuera de rango en declaración " + p[1])
                    else:
                        print("Tamaño de String es incompatible en " + p[1])
                else:
                    print("Error en la definicion de " + p[1])
            else:
                print("Error en la definicion de " + p[1])
        else:
            if isinstance(variables[p[1]][0], list):
                if isinstance(p[6], int):
                    if len(variables[p[1]][0]) > p[3]:
                        # excecute.change_atomic('String', p[3])
                        variables[p[1]][0][p[3]] = p[6]
                    elif len(variables[p[1]][0]) == p[3]:
                        variables[p[1]][0].append(p[6])
                    else:
                        print("Indice fuera de rango en declaración " + p[1])
                else:
                    print("Error en la definicion de " + p[1])
            else:
                    print("Error en la definicion de " + p[1])

#     # if variables[p[1][1]] == 'String':
#     #     if isinstance(variables[p[1][0]], list):
#     #         if isinstance(p[6], str):
#     #             try:
#     #                 variables[p[1][0][p[3]]] = p[6]
#     #             except:
#     #                 if
#     # if variables[p[1][1]] == 'Int':
#     #
#     # if p[2] == '=':
#     #     if not isinstance(variables[p[1]][0], list):
#     #         if p[]
#     #         variables[p[1]] = p[3]
#     #         print(('=', p[1], p[3]))
#     # elif p[5] == '=':
#     #     print(('=', p[1] + p[2] + p[3] + p[4], p[5]))
#     #     variables[p[1]][3] = p[6]



def p_Inc(p):
    '''
    Inc : INC LPAREN ID COMMA NUMBER RPAREN
    '''
    global variables, loop_array
    if isinstance(variables[p[3]][0], int):
        loop_array.append(['Inc', p[3], p[5]])
    else:
        print("Syntax error number in for is not an int")

def p_Dec(p):
    '''
    Dec : DEC LPAREN ID COMMA NUMBER RPAREN
    '''
    global variables, loop_array
    if isinstance(variables[p[3]][0], int):
        loop_array.append(['Dec', p[3], p[5]])
    else:
        print("Syntax error number in for is not an int")

def p_Body(p):
    '''
    Body : Inc Body
         | Dec Body
         | RANDOM Body
         | empty
    '''
    p[0] = p[1]

def p_For(p):
    '''
    For : FOR NUMBER TIMES USING ID Body FOREND SEMCOL
    '''
    global variables, loop_array
    # if isinstance(variables[p[5]][0], list):
    #     loop_array.append(p[2])
    # else:
    print(variables)
    loop_array.append(p[2])
    variables = ex.loop(loop_array, variables)
    print(variables)
    loop_array = []
        

def p_Dow(p):
    '''
    Dow : DOW LPAREN ID RPAREN Body ENDDO SEMCOL
        | DOW LPAREN NUMBER RPAREN Body ENDDO SEMCOL
    '''
    global variables, loop_array
    if isinstance(p[3], int):
        loop_array.append(p[3])
    else:
        loop_array.append(variables[p[3]][0])
    print(variables)
    ex.loop(loop_array, variables)
    print(variables)
    loop_array = []

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None

def p_type(p):
    '''
    TYPE : INT
         | STRING LPAREN NUMBER RPAREN
    '''
    if p[1] == 'Int':
        p[0] = [p[1]]
    elif p[1] == 'String':
        p[0] = [p[1], p[3]]

def p_atomic(p):
    '''
    ATOMIC : NUMBER
           | TEXT
    '''
    p[0] = p[1]

# def p_Random():
#     '''
#     Random : RANDOM LPAREN ID COMMA ID COMMA ID RPAREN SEMICOL
#     '''
#     p[0] = p[1]


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