def p_statements(p):
    '''
    statements : var_assign statements
               | var_define statements
               | For statements
               | empty
    '''
    print(p)