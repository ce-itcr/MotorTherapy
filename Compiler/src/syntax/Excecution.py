# def change_array(Type, data, index, array_size):
#     True
#
# def change_atomic(Type, data):
def for_index(for_array, variables):
    for i in range(len(for_array) - 1):
        if for_array[i][0] == 'Inc':
            variables[for_array[i][1]][0] += for_array[-1] * for_array[i][2]
        elif for_array[i][0] == 'Dec':
            variables[for_array[i][1][0]][0] -= for_array[-1] * for_array[i][2]
    return variables
