rows = []
conditions = []
with open('data12.txt', 'r') as file:
    for line in file:
        line = line.strip().split()
        newLine = line[0]
        rows.append(newLine)
        cond = line[1].split(',')
        cond2 = []
        for i in cond:
            cond2.append(int(i))
        conditions.append(cond2)
print(rows)
print(conditions)

def isValid(row, cond):
    row = row.split('.')
    row = [i for i in row if i != '']
    if len(row) != len(cond):
        return 0
    for i in range(len(row)):
        if len(row[i]) != cond[i]:
            return 0
    return 1

def fill(row, cond, unknowns, iter):
    if iter == len(unknowns):
        return isValid(row, cond)
    row = row[:unknowns[iter]]+'#'+row[unknowns[iter]+1:]
    result1 = fill(row, cond, unknowns, iter+1)
    row = row[:unknowns[iter]]+'.'+row[unknowns[iter]+1:]
    result2 = fill(row, cond, unknowns, iter+1)
    return result1 + result2

totalSum = 0
for i in range(len(rows)):
    row = rows[i]
    unknown = [i for i in range(len(row)) if row[i] == '?']
    possibleOutcome = fill(row, conditions[i], unknown, 0)
    totalSum += possibleOutcome
    print("row ", i, ' ', possibleOutcome)
print(totalSum)
