import random


# def change_array(Type, data, index, array_size):
#     True
#
# def change_atomic(Type, data):
# def variables_to_variables(variables, variables):
#     for item in variables:
#         variables[item][0] = variables[item]
#     return variables

def loop(loop_array, variables, var):
    print("var: " + str(var))
    print("loop_array: " + str(loop_array))
    for i in range(loop_array[-1]):
        for n in range(len(loop_array)-1):
            if loop_array[n][0] == 'Inc':
                if loop_array[n][2] == 'Local':
                    variables[loop_array[n][1]][0] += i
                else:
                    variables[loop_array[n][1]][0] += loop_array[n][2]
                print(variables[loop_array[n][1]])
            elif loop_array[n][0] == 'Dec':
                if loop_array[n][2] == 'Local':
                    variables[loop_array[n][1]][0] -= i
                else:
                    variables[loop_array[n][1]][0] -= loop_array[n][2]
            elif loop_array[n][0] == 'Balloon':
                print("balloon: " + str(variables['Balloons']))
                if isinstance(loop_array[n][0], int):
                    if isinstance(loop_array[n][1], int):
                        variables['Balloons'].append([loop_array[n][0], loop_array[n][1]])
                    else:
                        variables['Balloons'].append([loop_array[n][0], variables[loop_array[n][1]][0]])
                else:
                    if isinstance(loop_array[n][1], int):
                        variables['Balloons'].append([variables[loop_array[n]][0], loop_array[n][1]])
                    else:
                        variables['Balloons'].append([variables[loop_array[n][1]][0], variables[loop_array[n][2]][0]])
                print(variables[loop_array[n][1]])
            elif loop_array[n][0] == 'Random':
                if isinstance(var, list):
                    try:
                        if isinstance(variables[loop_array[n][1]][0], list):
                            variables[str(loop_array[n][0])+loop_array[n][1]].append(random_list(len(variables[loop_array[n][1]][0]), loop_array[n][2], variables[loop_array[n][1]][0]))
                        else:
                            variables[str(loop_array[n][0])+loop_array[n][1]].append(random_list(len(loop_array[n][1]), loop_array[n][2], loop_array[n][1]))
                    except:
                        print("loop_array")
                        variables[str(loop_array[n][0]) + loop_array[n][1]] = []
                        if isinstance(variables[loop_array[n][1]][0], list):
                            variables[str(loop_array[n][0])+loop_array[n][1]].append(random_list(len(variables[loop_array[n][1]][0]), loop_array[n][2], variables[loop_array[n][1]][0]))
                        else:
                            variables[str(loop_array[n][0])+loop_array[n][1]].append(random_list(len(loop_array[n][1]), loop_array[n][2], loop_array[n][1]))
                else:
                    try:
                        if isinstance(variables[var][0], list):
                            variables[str(loop_array[n][0])+var].append(random_list(len(variables[var][0]), loop_array[n][2], variables[var][0]))
                        else:
                            variables[str(loop_array[n][0])+var].append(random_list(len(var), loop_array[n][2], var))
                    except:
                        variables[str(loop_array[n][0]) + var] = []
                        if isinstance(variables[var][0], list):
                            variables[str(loop_array[n][0])+var].append(random_list(len(variables[var][0]), loop_array[n][2], variables[var][0]))
                        else:
                            variables[str(loop_array[n][0])+var].append(random_list(len(var), loop_array[n][2], var))

    return variables

def random_list(len_list, cant, array):
    print(array)
    if cant <= len_list:
        newList = []
        indexList = []
        for i in range(cant):
            newList.append("")
        counter = cant - 1
        a = random.randint(0, counter)
        for item in array:
            if len(indexList) < cant:
                while True:
                    if a in indexList:
                        a = random.randint(0, counter)
                    else:
                        indexList.append(a)
                        break
                print(item)
                newList[a] = item
            else:
                newList.append(item)
        print(newList)
    else:
        newList = array
        print("Error: Random contiene una cantidad mayor a la de la lista")
    return newList
