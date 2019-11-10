import ply.yacc as yacc
from src.lexical.Tokens import *
from src.syntax.Statements import *
import numpy
import src.syntax.Excecution as ex
import random

variables = {} # Balloons : [[x, y], [x, y]]
loop_array = []
start = 'statements'

# def p_game(p):
#     '''
#     Game : GAME LBRACE statements_excecute RBRACE END SEMICOL
#     '''
def p_Random(p):
    '''
    Random : RANDOM LPAREN ID COMMA atomic_variable COMMA atomic_variable RPAREN SEMCOL
    '''
    global variables
    try:
        ex.random_list(len(variables[p[3]][0]), int(p[5]), variables[p[3]][0])
    except:
        try:
            if isinstance(variables[p[5]][0], int):
                ex.random_list(len(variables[p[3]][0]), variables[p[5]][0], variables[p[3]][0])
            else:
                print("Se requiere un tipo int")
        except:
            print("Error: Random contiene un ID que no se ha iniciado")

def p_num_variable(p):
    '''
    atomic_variable : NUMBER
                    | ID
    '''
    p[0] = p[1]
    print(p[0])

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
            variables[p[2]] = [p[4], p[1][0], p[1][1]]
        except:
            print(("=", p[2], p[4]))
            variables[p[2]] = [p[4], p[1][0]]
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
                            variables[p[1]][0].append(str(p[6]))
                            print(variables)
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

def p_ForRandom(p):
    '''
    ForRandom : RANDOM LPAREN ID COMMA atomic_variable RPAREN SEMCOL
              | RANDOM LPAREN NUMBER COMMA atomic_variable RPAREN SEMCOL
              | RANDOM LPAREN ID COMMA atomic_variable COMMA atomic_variable RPAREN SEMCOL
    '''
    global loop_array, variables
    try:
        p[9]
        if isinstance(variables[p[3]][0], list):
            if isinstance(p[5], int):
                loop_array.append(['Random', p[3], p[5]])
            elif isinstance(variables[p[5]], int):
                loop_array.append(['Random', variables[p[3]], variables[p[5]][0]])
            else:
                print("Error")
        else:
            print("Error")
    except:
        if isinstance(p[3], int):
            loop_array.append(['Random', [], p[3]])
        elif isinstance(variables[p[3]][0], int):
            loop_array.append(['Random', [], variables[p[3]][0]])
        else:
            print("Error")


def p_BalloonFor(p):
    '''
    BalloonFor : BALLOON LPAREN ID COMMA ID RPAREN SEMCOL
               | BALLOON LPAREN ID COMMA NUMBER RPAREN SEMCOL
               | BALLOON LPAREN NUMBER COMMA ID RPAREN SEMCOL
               | BALLOON LPAREN NUMBER COMMA NUMBER RPAREN SEMCOL
    '''
    global loop_array, variables
    try:
        variables["Balloons"]
    except:
        variables["Balloons"] = []
    if isinstance(p[3], int) or isinstance(variables[p[3]][0], int):
        if isinstance(p[5], int) or isinstance(variables[p[5]][0], int):
            loop_array.append(['Balloon', p[3], p[5]])
        else:
            print("Error en: " + p[5])
    else:
        print("Error en: " + p[3])


def p_IncFor(p):
    '''
    IncFor : INC LPAREN ID COMMA atomic_variable RPAREN SEMCOL
    '''
    global variables, loop_array
    print("variables: " + str(variables))
    try:
        if isinstance(p[5], int):
            if isinstance(variables[p[3]][0], int):
                loop_array.append(['Inc', p[3], p[5]])
            else:
                print("Syntax error number in for is not an int")
        elif isinstance(variables[p[5]], int):
            if isinstance(variables[p[3]][0], int):
                loop_array.append(['Inc', p[3], variables[p[5]]])
    except:
        if isinstance(variables[p[3]][0], int):
            loop_array.append(['Inc', p[3], 'Local'])
        else:
            print("Error3")


def p_DecFor(p):
    '''
    DecFor : DEC LPAREN ID COMMA atomic_variable RPAREN SEMCOL
    '''
    global variables, loop_array
    try:
        if isinstance(p[5], int):
            if isinstance(variables[p[3]][0], int):
                loop_array.append(['Dec', p[3], p[5]])
            else:
                print("Syntax error number in for is not an int")
        else:
            print("Error1")
    except:
        if isinstance(variables[p[3]][0], int):
            loop_array.append(['Dec', variables[p[3]][0], 'Local'])
        else:
            print("Error2")

def p_Body(p):
    '''
    Body : IncFor Body
         | DecFor Body
         | BalloonFor Body
         | ForRandom Body
         | empty
    '''
    p[0] = p[1]

def p_For(p):
    '''
    For : FOR NUMBER TIMES USING ID Body FOREND SEMCOL
    '''
    # if isinstance(variables[p[5]][0], list):
    #     loop_array.append(p[2])
    # else:
    global variables, loop_array
    print("variables" + str(variables))
    loop_array.append(p[2])
    print("loop array: " + str(loop_array))
    try:
        if isinstance(variables[p[5]][0], list):
            variables = ex.loop(loop_array, variables, p[5])
    except:
        variables = ex.loop(loop_array, variables, 0)
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
    ex.loop(loop_array, variables, [])
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