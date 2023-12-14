lines = []
with open('data14.txt', 'r') as file:
    for line in file:
        line = line.strip().split()[0]
        lines.append(line)

height = len(lines)
stateDict = {}

def rollNorth(lines):
    newLines = ["" for _ in lines]
    for i in range(len(lines[0])):
        rocks = 0
        empties = 0
        for j in range(height):
            if lines[j][i] == 'O':
                rocks += 1
            if lines[j][i] == '.':
                empties += 1
            if lines[j][i] == '#':
                for k in range(rocks):
                    newLines[j-rocks-empties+k] += 'O'
                for k in range(empties):
                    newLines[j - empties + k] += '.'
                newLines[j] += '#'
                rocks = 0
                empties = 0
        for k in range(rocks):
            newLines[height - rocks - empties + k] += 'O'
        for k in range(empties):
            newLines[height - empties + k] += '.'
    return newLines

def rollWest(lines):
    newLines = []
    for i in range(height):
        rocks = 0
        empties = 0
        row = ""
        for j in range(len(lines[0])):
            if lines[i][j] == 'O':
                rocks += 1
            elif lines[i][j] == '.':
                empties += 1
            else:
                for k in range(rocks):
                    row += 'O'
                for k in range(empties):
                    row += '.'
                row += '#'
                rocks = 0
                empties = 0
        for k in range(rocks):
            row += 'O'
        for k in range(empties):
            row += '.'
        newLines.append(row)
    return newLines

def rollSouth(lines):
    newLines = ["" for _ in lines]
    for i in range(len(lines[0])):
        rocks = 0
        empties = 0
        for j in range(height):
            if lines[j][i] == 'O':
                rocks += 1
            if lines[j][i] == '.':
                empties += 1
            if lines[j][i] == '#':
                for k in range(empties):
                    newLines[j - rocks - empties + k] += '.'
                for k in range(rocks):
                    newLines[j-rocks+k] += 'O'
                newLines[j] += '#'
                rocks = 0
                empties = 0
        for k in range(empties):
            newLines[height -rocks-empties + k] += '.'
        for k in range(rocks):
            newLines[height - rocks + k] += 'O'
    return newLines

def rollEast(lines):
    newLines = []
    for i in range(height):
        rocks = 0
        empties = 0
        row = ""
        for j in range(len(lines[0])):
            if lines[i][j] == 'O':
                rocks += 1
            elif lines[i][j] == '.':
                empties += 1
            else:
                for k in range(empties):
                    row += '.'
                for k in range(rocks):
                    row += 'O'
                row += '#'
                rocks = 0
                empties = 0
        for k in range(empties):
            row += '.'
        for k in range(rocks):
            row += 'O'
        newLines.append(row)
    return newLines

def roll(lines):
    return rollEast(rollSouth(rollWest(rollNorth(lines))))

def cHash(lines):
    longString = ""
    for line in lines:
        longString += line
    return hash(longString)

iter = 0
while iter < 10**9:
    stateHashed = cHash(lines)
    if stateHashed in stateDict.values():
        result_keys = [key for key, value in stateDict.items() if value == stateHashed]
        interval = iter - result_keys[0]
        iter += (int((10**9-iter)/interval))*interval
    else:
        stateDict[iter] = (cHash(lines))
    iter += 1
    lines = roll(lines)

bigSum = 0
for i in range(len(lines)):
    for element in lines[i]:
        if element == 'O':
            bigSum += height-i
print(bigSum)

# zad2 94876