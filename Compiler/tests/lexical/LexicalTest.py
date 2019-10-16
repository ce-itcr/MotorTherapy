from src.lexical.Lexical import *


def lexical_test():
    print("Lexical_TEST")

    print("\nGame_TEST")
    game_test()

    print("\nLoops_TEST")
    loops_test()

    print("\nTypes_TEST")
    types_test()


def game_test():
    data = '''
    // Start of the game
    Begin

    Main { }
    
    // Balloons
    Game1 { }
    
    // Piano
    Game2 { }
    
    // CobWeb
    Game3 { }
    
    // Targets
    Game4 { }
    
    End;
    '''
    printTokens(consume(data))


def loops_test():
    data = '''
    // Loops
    Dow(i)
	Enddo;
	
	FOR 5 times using Color
    FOREND;
    
    ForAsignWord(rows, columns) DO
	AsignWord(words, points);
    '''
    printTokens(consume(data))


def types_test():
    data = '''
    // Types
    int x = 20 * 3 / 10;
    int y = 2 + x - 10;
    string(10) color[10];
    '''
    printTokens(consume(data))
