import ply.yacc as yacc
from src.lexical.Tokens import *
from src.syntax.Statements import *
from src.lexical.Errors import *
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
        variables["Random" + str(p[3])].append( ex.random_list(len(ex.value(p[3], variables, list)[1]), ex.value(p[5], variables, int)[1], ex.value(p[3], variables, list)[1]))
    except:
        variables["Random" + str(p[3])] = []
        variables["Random" + str(p[3])].append( ex.random_list(len(ex.value(p[3], variables, list)[1]), ex.value(p[5], variables, int)[1], ex.value(p[3], variables, list)[1]))
   
def p_atomic_variable(p):
    '''
    atomic_variable : NUMBER
                    | ID
                    | ID LSPAREN ID RSPAREN
                    | ID LSPAREN NUMBER RSPAREN
    '''
    try:
        p[0] = ex.value(p[1], variables, list)[1][ex.value(p[3], variables, int)[1]]
    except:
        p[0] = p[1]

def p_var_assign(p):
    '''
    var_assign : TYPE ID LSPAREN NUMBER RSPAREN SEMCOL
               | TYPE ID SEMCOL
    '''
    global variables, compilation_successful
    try:
        if variables[p[2]]:
            print("Error en asignacion: variable {0} ya existe".format(p[2]))
            compilation_successful = False
    except:
        if p[3] == '[':
            if p[1][0] == 'Int':
                variables[p[2]] = [[], p[1][0], p[4]]
            elif p[1][0] == 'String':
                variables[p[2]] = [[], p[1][0], p[4], p[1][1]] # dato, tipo, tamaño array, tamaño string
        else:
            try:
                variables[p[2]] = ["", p[1][0], p[1][1]]
            except:
                variables[p[2]] = [0, p[1][0]]


def p_var_define(p):
    '''
    var_define : ID EQUAL ATOMIC SEMCOL
               | ID LSPAREN NUMBER RSPAREN EQUAL ATOMIC SEMCOL
               | TYPE ID EQUAL ATOMIC SEMCOL
               | ID EQUAL atomic_variable SEMCOL
               | ID LSPAREN NUMBER RSPAREN EQUAL atomic_variable SEMCOL
               | ID LSPAREN ID RSPAREN EQUAL atomic_variable SEMCOL
    '''
    global variables, compilation_successful
    if p[3] == '=':
        try:
            if variables[p[2]]:
                print("Error en asignacion: variable {0} ya existe".format(p[2]))
                compilation_successful = False
        except:
            var_type = 0
            if p[1][0] == 'Int':
                var_type = int
            else:
                var_type = str
            try:
                if p[1][0] == 'String' and isinstance(p[4], var_type):
                    variables[p[2]] = [p[4], p[1][0], p[1][1]]
                else:
                    if var_type == int:
                        raise Exception
                    else:
                        print("Error en asignacion: tipo de variable incompatible en {0} ".format(p[2]))
            except:
                if isinstance(p[4], var_type):
                    variables[p[2]] = [p[4], p[1][0]]
                else:
                    print("Error en asignacion: tipo de variable incompatible en {0} ".format(p[2]))
    elif p[2] == '=':
        try:
            x = ex.value(p[3], variables, type(variables[p[1]][0]))
            if ex.validatedefineID(p[1], p[3], variables):
                variables[p[1]][0] = variables[p[3]][0]
            else:
                compilation_successful = False
        except:
            if variables[p[1]][1] == 'String':
                if isinstance(p[3], str):
                    if len(p[3]) <= variables[p[1]][2]:
                        variables[p[1]][0] = p[3]
                    else:
                        print("Error en definición de variable {0}: Tamaño de String es incompatible ".format(p[1]))
                        compilation_successful = False
                else:
                    print("Error en definición de variable {0}".format(p[1]))
                    compilation_successful = False
            else:
                if isinstance(p[3], int):
                    variables[p[1]][0] = p[3]
                else:
                    print("Error en definición de variable {0}".format(p[1]))
                    compilation_successful = False
    elif p[5] == '=':
        try:
            tp = 0
            if variables[p[1]][1] == 'Int':
                tp = int;
            else:
                tp = str;
            if isinstance(p[6], tp):
                if isinstance(variables[p[3]][0], str) or isinstance(variables[p[3]][0], list):
                    print("Error en definición de variable {0}".format(p[1]))
                    compilation_successful = False
                else:
                    if tp == str:
                        if variables[p[1]][3] >= len(ex.value(p[6], variables, tp)[1]):
                            if len(variables[p[1]][0]) < ex.value(p[3], variables, int)[1]:
                                variables[p[1]][0][ex.value(p[3], variables, int)[1]] = ex.value(p[6], variables, tp)[1]
                            elif len(variables[p[1]][0]) == ex.value(p[3], variables, int)[1]:
                                variables[p[1]][0].append = ex.value(p[6], variables, tp)[1]
                            else:
                                print("Error en definición de variable {0}: Indice fuera de rango".format(p[1]))
                                compilation_successful = False
                        else:
                            print("Error en definición de variable {0}: Tamaño de String es incompatible ".format(p[1]))
                            compilation_successful = False
                    else:
                        if len(variables[p[1]][0]) < ex.value(p[3], variables, int)[1]:
                            variables[p[1]][0][ex.value(p[3], variables, int)[1]] = ex.value(p[6], variables, tp)[1]
                        elif len(variables[p[1]][0]) == ex.value(p[3], variables, int)[1]:
                            variables[p[1]][0].append = ex.value(p[6], variables, tp)[1]
                        else:
                            print("Error en definición de variable {0}: Indice fuera de rango".format(p[1]))
                            compilation_successful = False
            else:
                print("Error en definición de variable {0}: tipo de variable o indice incompatible".format(p[1]))
                compilation_successful = False
        except:
            if variables[p[1]][1] == 'String':
                if isinstance(variables[p[1]][0], list):
                    if isinstance(p[6], str):
                        if len(p[6]) <= variables[p[1]][3]:
                            if len(variables[p[1]][0]) > p[3] and variables[p[1]][2] > p[3]:
                                variables[p[1]][0][p[3]] = p[6]
                            elif len(variables[p[1]][0]) == p[3] and variables[p[1]][2] > p[3]:
                                variables[p[1]][0].append(str(p[6]))
                            else:
                                print("Error en definición de variable {0}: Indice fuera de rango".format(p[1]))
                                compilation_successful = False
                        else:
                            print("Error en definición de variable {0}: Tamaño de String es incompatible ".format(p[1]))
                            compilation_successful = False
                    else:
                        print("Error en definición de variable {0}".format(p[1]))
                        compilation_successful = False
                else:
                    print("Error en definición de variable {0}".format(p[1]))
                    compilation_successful = False
            else:
                if isinstance(variables[p[1]][0], list):
                    if isinstance(p[6], int):
                        if len(variables[p[1]][0]) > p[3] and variables[p[1]][2] > p[3]:
                            variables[p[1]][0][p[3]] = p[6]
                        elif len(variables[p[1]][0]) == p[3] and variables[p[1]][2] > p[3]:
                            variables[p[1]][0].append(p[6])
                        else:
                            print("Error en definición de variable {0}: Indice fuera de rango".format(p[1]))
                            compilation_successful = False
                    else:
                        print("Error en definición de variable {0}".format(p[1]))
                        compilation_successful = False
                else:
                    print("Error en definición de variable {0}".format(p[1]))
                    compilation_successful = False

def p_SpiderWeb(p):
    '''
     Spiderweb : SPIDERWEB LPAREN atomic_variable COMMA atomic_variable RPAREN SEMCOL
    '''
    global variables, compilation_successful
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
            print("Error en SpiderWeb: ID {0} no definida".format(p[3]))
            compilation_successful = False
    elif isinstance(p[3], int) and isinstance(p[5], str):
        try:
            rows = p[3]
            columns = variables[p[5]][0]
        except:
            rows = 0
            columns = 0
            print("Error en SpiderWeb: ID {0} no definida".format(p[5]))
            compilation_successful = False
    else:
        try:
            rows = variables[p[3]][0]
            columns = variables[p[5]][0]
        except:
            rows = 0
            columns = 0
            print("Error en SpiderWeb: ID {0} y {1} no definidas ".format(p[5],p[3]))
            compilation_successful = False
    if rows and columns:
        variables['spiderWeb'] = [[], rows, columns]

def p_ForAssignWord(p):
    '''
    ForAssignWord : FORASIGNWORD LPAREN atomic_variable COMMA atomic_variable RPAREN DO ASIGNWORD LPAREN ID COMMA atomic_variable RPAREN SEMCOL
    '''
    global variables, compilation_successful
    try:
        if isinstance(variables['spiderWeb'][0], list):
            if ex.value(p[3], variables, int)[1] <= variables['spiderWeb'][1]:
                if ex.value(p[5], variables, int)[1] <= variables['spiderWeb'][2]:
                    try:
                        if isinstance(ex.value(p[12], variables, list)[1][0], int):
                            variables['spiderWeb'] = ex.assignValueSpiderWeb(variables, p[3], p[5], p[12], p[10])
                        else:
                            print("Error en ForAsignWord: La lista no es de numeros")
                            compilation_successful = False
                    except:
                        if ex.value(p[12], variables, int)[0]:
                            variables['spiderWeb'] = ex.assignValueSpiderWeb(variables, p[3], p[5], p[12], p[10])
                        else:
                            print("Error en ForAsignWord: score no es un numero")
                            compilation_successful = False
                else:
                    print("Error en ForAsignWord: Numero de columnas invalido")
                    compilation_successful = False
            else:
                print("Error en ForAsignWord: Numero de filas invalido")
                compilation_successful = False
    except:
        print("Error en ForAsignWord")
        compilation_successful = False

def p_Inc(p):
    '''
    Inc : INC LPAREN ID COMMA atomic_variable RPAREN SEMCOL
    '''
    global variables, compilation_successful
    try:
        variables[p[3]][0] += ex.value(p[5], variables, int)[1]
    except:
        print("Error en Inc: entrada inválida")
        compilation_successful = False


def p_Dec(p):
    '''
    Dec : DEC LPAREN ID COMMA atomic_variable RPAREN SEMCOL
    '''
    global variables, compilation_successful
    try:
        variables[p[3]][0] -= ex.value(p[5], variables, int)[1]
    except:
        print("Error en Dec: entrada inválida")
        compilation_successful = False

def p_RandomFor(p):
    '''
    RandomFor : RANDOM LPAREN ID COMMA atomic_variable RPAREN SEMCOL
              | RANDOM LPAREN NUMBER COMMA atomic_variable RPAREN SEMCOL
              | RANDOM LPAREN ID COMMA atomic_variable COMMA atomic_variable RPAREN SEMCOL
    '''
    global loop_array, variables, compilation_successful
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
                print("Error en Random: entrada inválida")
                compilation_successful = False
        else:
            print("Error en Random: entrada inválida")
            compilation_successful = False
    except:
        if isinstance(p[3], int):
            loop_array.append(['Random', [], p[3]])
        elif isinstance(variables[p[3]][0], int):
            loop_array.append(['Random', [], p[3]])
        else:
            print("Error en Random: entrada inválida")
            compilation_successful = False

def p_ObjectFor(p):
    '''
    ObjectFor : OBJECT LPAREN atomic_variable_for COMMA atomic_variable_for COMMA atomic_variable_for RPAREN SEMCOL
    '''
    global loop_array, variables, compilation_successful
    try:
        variables['Objects']
    except:
        variables['Objects'] = []
    try:
        array = ['Object', p[3], p[5], p[7]]
        for n in range(3):
            if not isinstance(array[n+1], list):
                array[n+1] = [array[n+1], -2]
        loop_array.append(array)
    except:
        print("Error en Objects dentro de For: entrada inválida")
        compilation_successful = False



def p_BalloonFor(p):
    '''
    BalloonFor : BALLOON LPAREN ID COMMA ID RPAREN SEMCOL
               | BALLOON LPAREN ID COMMA NUMBER RPAREN SEMCOL
               | BALLOON LPAREN NUMBER COMMA ID RPAREN SEMCOL
               | BALLOON LPAREN NUMBER COMMA NUMBER RPAREN SEMCOL
    '''
    global loop_array, variables, compilation_successful
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
        compilation_successful = False


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
        print("Error en Inc: entrada inválida")
        compilation_successful = False
        loop_array.append()

def p_DecFor(p):
    '''
    DecFor : DEC LPAREN ID COMMA atomic_variable RPAREN SEMCOL
    '''
    global variables, loop_array, compilation_successful
    try:
        if not ex.value(p[3], variables, int)[0]:
            if ex.value(p[5], variables, int)[0]:
                loop_array.append(['Dec', p[3], p[5]])
            elif not ex.value(p[5], variables, int)[0]:
                loop_array.append(['Dec', p[3], variables[p[5]][0]])
    except:
        print("Error en DecFor: entrada inválida")
        compilation_successful = False
        loop_array = []

def p_Body(p):
    '''
    Body : IncFor Body
         | DecFor Body
         | BalloonFor Body
         | RandomFor Body
         | ObjectFor Body
         | empty
    '''
    p[0] = p[1]

def p_For(p):
    '''
    For : FOR NUMBER TIMES USING ID Body FOREND SEMCOL
    '''
    global variables, loop_array
    loop_array.append(p[2])
    try:
        if isinstance(variables[p[5]][0], list):
            variables = ex.loop(loop_array, variables, p[5])
    except:
        variables = ex.loop(loop_array, variables, 0)
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
    elif p[2] == '(':
        p[0] = [p[1], p[3]]

def p_atomic(p):
    '''
    ATOMIC : NUMBER
           | TEXT
    '''
    p[0] = p[1]

def p_atomic_variable_for(p):
    '''
    atomic_variable_for : ID LSPAREN atomic_variable RSPAREN
                        | ID
                        | NUMBER
    '''
    global variables
    try:
        if isinstance(ex.value(p[1], variables, list)[1], list):
            try:
                if ex.value(p[3], variables, int)[1] + 1:
                    True
                p[0] = [p[1], p[3]]
            except:
                p[0] = [p[1], -1]
    except:
        p[0] = p[1]

def p_error(p):
    global compilation_successful
    if not p:
        exit(1)
    compilation_successful = False
    print("Error sintáctico en linea {0}".format(p.lineno))
    exit(1)
parser = yacc.yacc()