main_instructions = []

def p_statements_test(p):
    # BEGIN games END SEMICOL
    '''
    statements : var_assign statements
               | var_define statements
               | For statements
               | Dow statements
               | Inc statements
               | Dec statements
               | Random statements
               | Spiderweb statements
               | ForAssignWord statements
               | empty
    '''
    print(p)
#
# def p_games_test(p):
#     '''
#     games : BEGIN GAME1 LBRACE statements RBRACE GAME2 LBRACE statements etc
#     '''
#
#
# # Code Excecution
#
# def p_start(p):
#     '''
#     start : BEGIN MAIN LBRACE statements_excecute RBRACE END SEMICOL
#     '''
#
#
# def p_statements(p):
#     '''
#     statements : var_assign statements
#                | var_define statements
#                | For statements
#                | Dow statements
#                | Game statements
#                | empty
#     '''
#
