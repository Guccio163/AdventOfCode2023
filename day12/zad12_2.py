from copy import deepcopy

rows = []
conditions = []
with open('data12.txt', 'r') as file:
    for line in file:
        line = line.strip().split()
        rows.append((line[0] + '?') * 4 + line[0])
        conditions.append([int(i) for _ in range(5) for i in line[1].split(',')])

def getSpaces(row):
    return [i for i in row.split('.') if i != ' ' and i != '']

def skipFirst(row):
    newRow = row
    temp = newRow[0][1:]
    if temp == '':
        return newRow[1:]
    newRow[0] = temp
    return newRow

def fillFirst(row, cond):
    newRow = row
    if len(row[0]) == cond or len(row[0])+1 == cond:
        return newRow[1:]
    else:
        temp = newRow[0][cond+1:]
        if temp == '':
            return newRow[1:]
        newRow[0] = temp
        return newRow

def checkForHash(row):
    for interval in row:
        if '#' in interval:
            return False
    return True

def getDigits(row):
    suma = 0
    for interval in row:
        suma += len(interval)
    return suma

resultsArray = [[] for _ in rows]
def getAllPossiblities(rowArg, conds, i):

    digits = getDigits(rowArg)
    if resultsArray[i][len(conds)][digits] != -1:
        return resultsArray[i][len(conds)][digits]

    row = deepcopy(rowArg)
    if conds == []:
        if checkForHash(row):
            resultsArray[i][len(conds)][digits] = 1
            return 1
        resultsArray[i][len(conds)][digits] = 0
        return 0
    if row == []:
        resultsArray[i][len(conds)][digits] = 0
        return 0

    while len(row[0]) < conds[0] or len(row) == 0:

        if '#' not in row[0]:
            row = row[1:]
            if row == []:
                resultsArray[i][len(conds)][digits] = 0
                return 0
        else:
            resultsArray[i][len(conds)][digits] = 0
            return 0

    if row[0][0] == '#':
        if len(row[0]) < conds[0]:
            print("should not occur")
            return 0
        if len(row[0]) > conds[0]:
            if row[0][conds[0]] == '#':
                resultsArray[i][len(conds)][digits] = 0
                return 0
        res = getAllPossiblities(fillFirst(row, conds[0]), conds[1:], i)
        resultsArray[i][len(conds)][digits] = res
        return res

    if len(row[0]) > conds[0]:
        if row[0][conds[0]] == '#':
            res = getAllPossiblities(skipFirst(row), conds, i)
            resultsArray[i][len(conds)][digits] = res
            return res

    result = getAllPossiblities(fillFirst(deepcopy(row), conds[0]), conds[1:], i) + getAllPossiblities(skipFirst(deepcopy(row)), conds, i)
    resultsArray[i][len(conds)][digits] = result
    return result

totalSum = 0
for i in range(len(rows)):
    resultsArray[i] = [[-1 for _ in range(len(rows[i])+1)] for _ in range(len(conditions[i])+1)]
    newRows = [getSpaces(row) for row in rows]
    totalSum += getAllPossiblities(newRows[i], conditions[i], i)

print(totalSum)

# 1 566 786 613 613 is the correct answer
# damn, that took way too long