import random


# def change_array(Type, data, index, array_size):
#     True
#
# def change_atomic(Type, data):
# def variables_to_variables(variables, variables):
#     for item in variables:
#         variables[item][0] = variables[item]
#     return variables

def value(var, variables, t):
    try:
        if isinstance(var, t):
            return [True, var]
        elif isinstance(variables[var][0], t):
            return [False, variables[var][0]]
    except:
        return

def loop(loop_array, variables, var):
    if isinstance(var, str):
        var_str = True
    else:
        var_str = False
    print("variables: " + str(variables))
    print("var: " + str(var))
    print("loop_array: " + str(loop_array))
    for i in range(loop_array[-1]):
        for n in range(len(loop_array)-1):
            if loop_array[n][0] == 'Inc':
                if loop_array[n][2] == 'Local':
                    variables[loop_array[n][1]][0] += i
                else:
                    variables[loop_array[n][1]][0] += value(loop_array[n][2], variables, int)[1]
            elif loop_array[n][0] == 'Dec':
                if loop_array[n][2] == 'Local':
                    variables[loop_array[n][1]][0] -= i
                else:
                    variables[loop_array[n][1]][0] -= value(loop_array[n][2], variables, int)[1]
            elif loop_array[n][0] == 'Balloon':
                x = value(loop_array[n][1], variables, int)[1]
                y = value(loop_array[n][2], variables, int)[1]
                variables['Balloons'].append([x, y])
            elif loop_array[n][0] == 'Random':
                var_val_list = value(var, variables, list)
                var_val_int = value(var, variables, int)
                ran_arr = loop_array[n][1]
                if var_str:
                    str_name = 'Random' + var
                else:
                    str_name = 'Random' + ran_arr
                print("ran_arr = " + str(ran_arr))
                if value(ran_arr, variables, list)[1] == []:
                    try:
                        variables[str_name]
                    except:
                        variables[str_name] = []
                ran_arr_val = value(ran_arr, variables, list)
                try:
                    var_val_int[0]
                    if ran_arr_val[0]:
                        variables[str_name].append(random_list(len(ran_arr_val[1]), var_val_int[1], ran_arr_val[1]))
                    else:
                        print("Error en RandomFor")
                except:
                    if ran_arr_val[0]:
                        list_to_append = random_list(len(var_val_list[1]), value(loop_array[n][2], variables, int)[1], var_val_list[1])
                        if list_to_append != None:
                            variables[str_name].append(list_to_append)
                    else:
                        print("Error en RandomFor")
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
        print(newList)
        return newList
    else:
        newList = array
        print("Error: Random contiene una cantidad mayor a la de la lista")

def assignValueSpiderWeb(variables, rowsID, columnsID, scoreID, wordsID):
    spiderWeb = []
    counter = 0
    counterWords = 0
    if value(rowsID, variables, int)[0]:
        if value(columnsID, variables, int)[0]:
            for i in range(columnsID):
                tempList = []
                for j in range(rowsID):
                    try:
                        tempList.append([variables[wordsID][0][counterWords], variables[scoreID][0][counter]])
                        if counter < len(variables[wordsID][0]):
                            counter += 1
                        else:
                            counter = 0
                        counterWords += 1
                    except:
                        tempList.append([variables[wordsID][0][counterWords], scoreID])
                        counterWords += 1
                spiderWeb.append(tempList)
            print(spiderWeb)
        else:
            for i in range(variables[columnsID][0]):
                tempList = []
                for j in range(rowsID):
                    try:
                        tempList.append([variables[wordsID][0][counterWords], variables[scoreID][0][counter]])
                        if counter < len(variables[wordsID][0]):
                            counter += 1
                        else:
                            counter = 0
                        counterWords += 1
                    except:
                        tempList.append([variables[wordsID][0][counterWords], scoreID])
                        counterWords += 1
                spiderWeb.append(tempList)
            print(spiderWeb)
    else:
        if value(columnsID, variables, int)[0]:
            for i in range(columnsID):
                tempList = []
                for j in range(variables[rowsID][0]):
                    try:
                        tempList.append([variables[wordsID][0][counterWords], variables[scoreID][0][counter]])
                        if counter < len(variables[wordsID][0]):
                            counter += 1
                        else:
                            counter = 0
                        counterWords += 1
                    except:
                        tempList.append([variables[wordsID][0][counterWords], scoreID])
                        counterWords += 1
                spiderWeb.append(tempList)
            print(spiderWeb)
        else:
            for i in range(variables[columnsID][0]):
                tempList = []
                for j in range(variables[rowsID][0]):
                    try:
                        tempList.append([variables[wordsID][0][counterWords], variables[scoreID][0][counter]])
                        if counter < len(variables[wordsID][0]):
                            counter += 1
                        else:
                            counter = 0
                        counterWords += 1
                    except:
                        tempList.append([variables[wordsID][0][counterWords], scoreID])
                        counterWords += 1
                spiderWeb.append(tempList)
            print(spiderWeb)
    return spiderWeb


def validatedefineID(ID1, ID2, variables):
    print("1")
    if variables[ID1][1] == variables[ID2][1]:
        print("2")
        if isinstance(variables[ID1][0], type(variables[ID2][0])):
            print("3")
            if variables[ID1][1] == 'String' and isinstance(variables[ID1][0], str):
                print(variables[ID1], variables[ID2][0])
                if variables[ID1][2] >= len(variables[ID2][0]) - 2:
                    print("success")
                    return True
                else:
                    print("Error: Tamaño de String es incompatible en " + ID1)
                    return False
            elif variables[ID1][1] == 'Int' and isinstance(variables[ID1][0], int):
                return True
            else:
                if variables[ID1][1] == 'String':
                    if variables[ID1][3] >= len(variables[ID2][0]) - 2:
                        if variables[ID1][2] >= variables[ID2][2]:
                            return True
                        else:
                            print("Error: Tamaño de arrays es incompatible en " + ID1)
                            return False
                    else:
                        print("Error: Tamaño de String es incompatible en " + ID1)
                        return False
                else:
                    if variables[ID1][2] >= variables[ID2][2]:
                        return True
                    else:
                        print("Error: Tamaño de arrays es incompatible en " + ID1)
                        return False
        else:
            print("Error: tipos de variables incompatible en " + ID1)
            return False
    else:
        print("Error: tipos de variables incompatible en " + ID1)
        return False