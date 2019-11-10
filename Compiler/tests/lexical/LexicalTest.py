from src.lexical.Lexical import *
import src.syntax.Syntax as syn
from src.syntax.Statements import *


ok = "OK"


# Main function to run the test
def lexical_test():
    print("\nLexical_TEST running... ")

    # game_test()
    loops_test()
    # types_test()
    # symbols_test()
    # functions_test()
    # operators_test()
    # containers_test()

    # print(ok)


def game_test():
    # print("\tGame_TEST running... ", end='')

    data = '''
    // Start of the game
    Begin
    Main { }
    Game1 { }
    Game2 { }
    Game3 { }
    Game4 { }
    End;
    '''
    # consume(data)

    print(ok)


def loops_test():
    print("\tLoops_TEST running... ", end='')

#     Dow(5)
#     Balloon(y, x);
#     Balloon(x, y);
#     Inc(x, 1);
#     Inc(y, 1);
#     Inc(y, 1);
#     Inc(y, 1);
#     Inc(y, 1);
#     Inc(y, 1);
#     Inc(y, 1);
#     Inc(y, 1);
#     Inc(y, 1);
#     Inc(y, 1);
#     Inc(y, 1);
#     Inc(y, 1);
#     Inc(y, 1);
#     Inc(y, 1);
#     Inc(y, 1);
#     Inc(y, 1);
#     Inc(y, 1);
#
#
# Enddo;
    data = '''
    // Loops
    Int x = 1;
    Int y = 1;
    String(10) color[4];
    color[0] = "blue";
    color[1] = "red";
    color[2] = "green";
    color[3] = "yellow";
    color[4] = "purple";
    FOR 5 Times Using color
        Inc(x, i);
        Random(3, 5);
    FOREND;
    '''

    # print(consume(data))
    syn.parser.parse(data)
    print(ok)


def types_test():
    print("\tTypes_TEST running... ", end='')

    # data = '''
    # Int a = 5;
    # String(4) r;
    # String(10) color[10];
    # a = 9;
    # a = "hola";
    # r = "holapo";
    # color[5] = "uopj";
    # color[0] = "adios";
    # '''
    data = '''
    String(10) color[4];
    color[0] = "blue";
    color[1] = "red";
    color[2] = "green";
    color[3] = "yellow";
    color[4] = "purple";
    Random(color, 3, 5);
    '''
    # print(consume(data))
    syn.parser.parse(data)
    print(ok)


def symbols_test():
    print("\tSymbols_TEST running... ", end='')

    data = '''
    // Symbols
    x = 29876;
    myName = "Jose Daniel";
    comma = ,
    '''
    # consume(data)
    print(ok)


def functions_test():
    print("\tFunctions_TEST running... ", end='')

    data = '''
    // Functions
    Balloon();
    Inc();
    Dec();
    Random();
    ForAsignWord();
    AsignWord();
    Object();
    SpiderWeb();
    '''
    # consume(data)
    print(ok)


def operators_test():
    print("\tOperators_TEST running... ", end='')

    data = '''
        // Operators
        = + - * /
        '''
    # consume(data)
    print(ok)


def containers_test():
    print("\tContainers_TEST running... ", end='')

    data = '''
        // Containers
        () [] {}
        '''
    # consume(data)
    print(ok)
