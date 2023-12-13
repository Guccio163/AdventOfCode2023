lines = []
with open('data13.txt', 'r') as file:
    buffer = []
    for line in file:
        line = line.strip().split()
        if(line == []):
            lines.append(buffer)
            buffer = []
        else:
            buffer.append(line[0])
def checkForHorMirror(sett, i):
    errors = 0
    for j in range(min(i + 1, len(sett) - 1 - i)):
        if sett[i - j] != sett[i + j + 1]:
            for k in range(len(sett[i-j])):
                if sett[i - j][k] != sett[i + j + 1][k]:
                    errors += 1
    return errors

def checkForVerMirror(sett, i):
    errors = 0
    for j in range(min(i + 1, len(sett[0]) - 1 - i)):
        for line in sett:
            if line[i - j] != line[i + j + 1]:
                errors += 1
    return errors

def solve(errors_):
    bigSum = 0
    for sett in lines:
        errors = 0
        for i in range(len(sett)-1):
            if checkForHorMirror(sett, i) == errors_ and errors == 0:
                errors += errors_
                bigSum += 100*(i+1)
        for i in range(len(sett[0])-1):
            if checkForVerMirror(sett, i) == errors_ and errors == 0:
                errors += errors_
                bigSum += i+1
    return bigSum

print(solve(0))
print(solve(1))

# zad1: 37975
# zad2: 32497