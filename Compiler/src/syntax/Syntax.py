import ply.yacc as yacc
from src.lexical.Tokens import *
from src.syntax.Statements import *
import numpy
import src.syntax.Excecution as ex
import random

variables = {} # Balloons : [[x, y], [x, y]]
loop_array = []
start = 'statements'
compilation_successful = True

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
                print("Error en Random: Se requiere un tipo int")
        except:
            print("Error: Random contiene un ID que no se ha iniciado")

def p_num_variable(p):
    '''
    atomic_variable : NUMBER
                    | ID
    '''
    p[0] = p[1]

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
            variables[p[2]] = ["", p[1][0], p[1][1]]
            print(("Created", p[2]))
        except:
            variables[p[2]] = [0, p[1][0]]
            print(("Created", p[2]))


def p_var_define(p):
    '''
    var_define : ID EQUAL ATOMIC SEMCOL
               | ID LSPAREN NUMBER RSPAREN EQUAL ATOMIC SEMCOL
               | TYPE ID EQUAL ATOMIC SEMCOL
               | ID EQUAL ID SEMCOL
    '''
    global variables, compilation_successful
    if p[3] == '=':
        try:
            variables[p[2]] = [p[4], p[1][0], p[1][1]]
        except:
            print(("=", p[2], p[4]))
            variables[p[2]] = [p[4], p[1][0]]
    elif p[2] == '=':
        try:
            x = ex.value(p[3], variables, type(variables[p[1]][0]))
            print(variables)
            if ex.validatedefineID(p[1], p[3], variables):
                variables[p[1]][0] = variables[p[3]][0]
                print(variables)
            else:
                compilation_successful = False
        except:
            if variables[p[1]][1] == 'String':
                if isinstance(p[3], str):
                    if len(p[3]) <= variables[p[1]][2]:
                        # excecute.change_atomic('String', p[3])
                        variables[p[1]][0] = p[3]
                    else:
                        print("Error: Tamaño de String es incompatible en " + p[1])
                        compilation_successful = False
                else:
                    print("Error en la definicion de " + p[1])
                    compilation_successful = False
            else:
                if isinstance(p[3], int):
                    # excecute.change_atomic('Int', p[3])
                    print(("=", p[1], p[3]))
                    variables[p[1]][0] = p[3]
                else:
                    print("Error en la definicion de " + p[1])
                    compilation_successful = False
    elif p[5] == '=':
        if variables[p[1]][1] == 'String':
            if isinstance(variables[p[1]][0], list):
                if isinstance(p[6], str):
                    if len(p[6]) <= variables[p[1]][3]:
                        if len(variables[p[1]][0]) > p[3] and variables[p[1]][2] > p[3]:
                            # excecute.change_atomic('String', p[3])
                            variables[p[1]][0][p[3]] = p[6]
                        elif len(variables[p[1]][0]) == p[3] and variables[p[1]][2] > p[3]:
                            variables[p[1]][0].append(str(p[6]))
                            print(variables)
                        else:
                            print("Indice fuera de rango en declaración " + p[1])
                            compilation_successful = False
                    else:
                        print("Tamaño de String es incompatible en " + p[1])
                        compilation_successful = False
                else:
                    print("Error en la definicion de " + p[1])
                    compilation_successful = False
            else:
                print("Error en la definicion de " + p[1])
                compilation_successful = False
        else:
            if isinstance(variables[p[1]][0], list):
                if isinstance(p[6], int):
                    if len(variables[p[1]][0]) > p[3] and variables[p[1]][2] > p[3]:
                        # excecute.change_atomic('String', p[3])
                        variables[p[1]][0][p[3]] = p[6]
                    elif len(variables[p[1]][0]) == p[3] and variables[p[1]][2] > p[3]:
                        variables[p[1]][0].append(p[6])
                    else:
                        print("Indice fuera de rango en declaración " + p[1])
                        compilation_successful = False
                else:
                    print("Error en la definicion de " + p[1])
                    compilation_successful = False
            else:
                print("Error en la definicion de " + p[1])
                compilation_successful = False

def p_SpiderWeb(p):
    '''
     Spiderweb : SPIDERWEB LPAREN atomic_variable COMMA atomic_variable RPAREN SEMCOL
    '''
    global variables
    print(variables)
    rows = 0
    columns = 0
    if isinstance(p[3], int) and isinstance(p[5], int):
        rows = p[3]
        columns = p[5]
    elif isinstance(p[3], str) and isinstance(p[5], int):
        try:
            rows = variables[p[3]][0]
            columns = p[5]
        except:
            rows = 0
            columns = 0
            print("ID no definida " + p[3])
    elif isinstance(p[3], int) and isinstance(p[5], str):
        try:
            rows = p[3]
            columns = variables[p[5]][0]
        except:
            rows = 0
            columns = 0
            print("ID no definida " + p[5])
    else:
        try:
            rows = variables[p[3]][0]
            columns = variables[p[5]][0]
        except:
            rows = 0
            columns = 0
            print("ID no definida " + p[5] + " y " + p[3])
    if rows and columns:
        # SpiderWeb = []
        # for i in range(columns):
        #     tempList = []
        #     for j in range(rows):
        #         tempList.append(["", 0])
        #     SpiderWeb.append(tempList)
        variables['spiderWeb'] = [[], rows, columns]
        print(variables)

def p_ForAssignWord(p):
    '''
    ForAssignWord : FORASIGNWORD LPAREN atomic_variable COMMA atomic_variable RPAREN DO ASIGNWORD LPAREN ID COMMA atomic_variable RPAREN SEMCOL
    '''
    global variables
    try:
        if isinstance(variables['spiderWeb'][0], list):
            if ex.value(p[3], variables, int)[1] <= variables['spiderWeb'][1]:
                if ex.value(p[5], variables, int)[1] <= variables['spiderWeb'][2]:
                    try:
                        if isinstance(ex.value(p[12], variables, list)[1][0], int):
                            variables['spiderWeb'] = ex.assignValueSpiderWeb(variables, p[3], p[5], p[12], p[10])
                        else:
                            print("La lista no es de numeros")
                    except:
                        if ex.value(p[12], variables, int)[0]:
                            variables['spiderWeb'] = ex.assignValueSpiderWeb(variables, p[3], p[5], p[12], p[10])
                        else:
                            print("score no es un numero")
                else:
                    print("Numero de columnas invalido")
            else:
                print("Numero de filas invalido")
    except:
        print("Error en for assign")

def p_ForRandom(p):
    '''
    ForRandom : RANDOM LPAREN ID COMMA atomic_variable RPAREN SEMCOL
              | RANDOM LPAREN NUMBER COMMA atomic_variable RPAREN SEMCOL
              | RANDOM LPAREN ID COMMA atomic_variable COMMA atomic_variable RPAREN SEMCOL
    '''
    global loop_array, variables
    try:
        variables["times"]
    except:
        variables["times"] = []
    try:
        p[9]
        if isinstance(variables[p[3]][0], list):
            if isinstance(p[5], int):
                loop_array.append(['Random', p[3], p[5]])
            elif isinstance(variables[p[5]], int):
                loop_array.append(['Random', variables[p[3]], p[5]])
            else:
                print("Error")
        else:
            print("Error")
    except:
        if isinstance(p[3], int):
            loop_array.append(['Random', [], p[3]])
        elif isinstance(variables[p[3]][0], int):
            loop_array.append(['Random', [], p[3]])
        else:
            print("Error en ForRandom")


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
    try:
        if isinstance(ex.value(p[3], variables, int)[1], int) and isinstance(ex.value(p[3], variables, int)[1], int):
            loop_array.append(['Balloon', p[3], p[5]])
        else:
            raise Exception
    except:
        print("Error en creación de globos: entrada inválida")


def p_IncFor(p):
    '''
    IncFor : INC LPAREN ID COMMA atomic_variable RPAREN SEMCOL
    '''
    global variables, loop_array, compilation_successful
    try:
        if isinstance(ex.value(p[3], variables, int)[1], int) and isinstance(ex.value(p[3], variables, int)[1], int):
            loop_array.append(['Inc', p[3], p[5]])
        else:
            raise Exception
    except:
        print("Error en Inc dentro de for: entrada inválida")
        compilation_successful = False
    # print("variables: " + str(variables))
    # try:
    #     if not ex.value(p[3], variables, int)[0]:
    #         if ex.value(p[5], variables, int)[0]:
    #             loop_array.append(['Inc', p[3], p[5]])
    #         elif not ex.value(p[5], variables, int)[0]:
    #             loop_array.append(['Inc', p[3], variables[p[5]][0]])
    # except:
    #     print("Error en IncFor")


def p_DecFor(p):
    '''
    DecFor : DEC LPAREN ID COMMA atomic_variable RPAREN SEMCOL
    '''
    global variables, loop_array
    try:
        if not ex.value(p[3], variables, int)[0]:
            if ex.value(p[5], variables, int)[0]:
                loop_array.append(['Dec', p[3], p[5]])
            elif not ex.value(p[5], variables, int)[0]:
                loop_array.append(['Dec', p[3], variables[p[5]][0]])
    except:
        print("Error en DecFor")

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
            print("p[5] = " + str(p[5]))
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
    global variables, loop_array, compilation_successful
    try:
        loop_array.append(ex.value(p[3], variables, int)[1])
        variables = ex.loop(loop_array, variables, [])
        print(variables)
    except:
        print("Error en Dow: entrada inválida")
        compilation_successful = False
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