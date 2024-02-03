lines = []
with open('data18.txt', 'r') as file:
    for line in file:
        line = line.strip().split()
        lines.append(line)
        # print(line)

curWidth = 1
width = 1
widthDown = 0
curHeight = 1
height = 1
heightDown = 0
for line in lines:
    if line[0] == 'D':
        curHeight += int(line[1])
        if curHeight > 0:
            height = max(height, curHeight)
    if line[0] == 'U':
        curHeight -= int(line[1])
        if curHeight < 0:
            heightDown = min(heightDown, curHeight)
    if line[0] == 'R':
        curWidth += int(line[1])
        if curWidth > 0:
            width = max(width, curWidth)
    if line[0] == 'L':
        curWidth -= int(line[1])
        if curWidth < 0:
            widthDown = min(widthDown, curWidth)
# print(width, widthDown, height, heightDown)

# so starting points are 70, 241 and dimentions are width: 341, height: 409

diggingboard = [[0 for _ in range(width-widthDown+20)] for _ in range(height-heightDown+20)]
currentPlace = [-1*heightDown+10, -1*widthDown+10]
currentDir = lines[0][0]
diggingboard[currentPlace[0]][currentPlace[1]] = 1
# lines.append(lines[0])
for line in lines:
    # if currentDir != line[0]:
    #     diggingboard[currentPlace[0]][currentPlace[1]] = 1
    #     currentDir = line[0]
    if line[0] == 'U':
        diggingboard[currentPlace[0]][currentPlace[1]] = 1
        for i in range(int(line[1])):
            currentPlace[0] -= 1
            diggingboard[currentPlace[0]][currentPlace[1]] = 1
    if line[0] == 'D':
        diggingboard[currentPlace[0]][currentPlace[1]] = 2
        for i in range(int(line[1])):
            currentPlace[0] += 1
            diggingboard[currentPlace[0]][currentPlace[1]] = 2
    if line[0] == 'R':
        for i in range(int(line[1])):
            currentPlace[1] += 1
            diggingboard[currentPlace[0]][currentPlace[1]] = 3
    if line[0] == 'L':
        for i in range(int(line[1])):
            currentPlace[1] -= 1
            diggingboard[currentPlace[0]][currentPlace[1]] = 3

for line in diggingboard:
    print(line)

# stan 3 oznacza że była 1 ale zamykająca, stan 4 że była 2 ale zamykająca
bigSum = 0
for i, line in enumerate(diggingboard):
    curElem = 0
    for j, element in enumerate(line):
        if element == 0 and (curElem == 1 or curElem == 2):
            diggingboard[i][j] = '4'
            bigSum += 1
        if element == 0 and not (curElem == 1 or curElem == 2):
            diggingboard[i][j] = '.'
        if element == 3:
            # diggingboard[i][j] = 4
            diggingboard[i][j] = '3'
            bigSum += 1
        if element == 1:
            diggingboard[i][j] = '1'
            bigSum += 1
            if curElem == 2:
                curElem = 3
            elif curElem in [0, 4]:
                curElem = 1
            # elif curElem == 3:
            #     bigSum += 1
        if element == 2:
            diggingboard[i][j] = '2'
            bigSum += 1
            if curElem == 1:
                curElem = 4
            elif curElem in [0, 3]:
                curElem = 2
            # elif curElem == 4:
            #     bigSum += 1
    print(bigSum)

print(bigSum)
for line in diggingboard:
    print(line)

# figure out shoelace area counting
#48 503