main_instructions = []

def p_statements_test(p):
    # BEGIN games END SEMICOL
    '''
    statements : var_assign statements
               | var_define statements
               | For statements
               | Dow statements
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
#     start : BEGIN MAIN LBRACE statements_excecute RBRACE
#     '''
#
# def p_statements_excecute(p):
#     '''
#     statements_exceute : var_assign statements
#                        | var_define statements
#                        | For statements
#                        | Dow statements
#                        | empty
#     '''
#     if p[1] == 'For':
#         main_instructions.append('For')
#     elif p[1] == 'Dow':
#         main_instructions.append('Dow')
#
