# def change_array(Type, data, index, array_size):
#     True
#
# def change_atomic(Type, data):
def loop(loop_array, variables):
    for i in range(len(loop_array) - 1):
        if loop_array[i][0] == 'Inc':
            variables[loop_array[i][1]][0] += loop_array[-1] * loop_array[i][2]
        elif loop_array[i][0] == 'Dec':
            variables[loop_array[i][1][0]][0] -= loop_array[-1] * loop_array[i][2]
    return variables
