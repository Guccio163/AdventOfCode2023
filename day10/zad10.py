from enum import Enum, auto

lines = []
map = []
with open('data10.txt', 'r') as file:
    for line in file:
        line = line.strip().split()[0]
        lines.append(line)
        map.append([0 for character in line])

class source(Enum):
    UP = auto()
    RIGHT = auto()
    DOWN = auto()
    LEFT = auto()

UP = source.UP
RIGHT = source.RIGHT
DOWN = source.DOWN
LEFT = source.LEFT

def changeS(y0, x0):
    twoSides = []
    if lines[y0 - 1][x0] in ['|', 'F', '7']:
        twoSides.append(UP)
    if lines[y0][x0 + 1] in ['-', 'J', '7']:
        twoSides.append(RIGHT)
    if lines[y0+1][x0] in ['|','J', 'L']:
        twoSides.append(DOWN)
    if lines[y0][x0-1] in ['-', 'F', 'L']:
        twoSides.append(LEFT)
    if RIGHT in twoSides:
        if LEFT in twoSides:
            return '-', RIGHT
        if UP in twoSides:
            return 'L', RIGHT
        if DOWN in twoSides:
            return 'F', RIGHT
    if LEFT in twoSides:
        if UP in twoSides:
            return 'J', LEFT
        if DOWN in twoSides:
            return '7', LEFT
    return '|', DOWN

def move(y, x, from_):
    currentChar = lines[y][x]

    if from_ is DOWN:
        if currentChar == '|':
            return y - 1, x, DOWN
        if currentChar == 'F':
            return y, x + 1, LEFT
        if currentChar == '7':
            return y, x - 1, RIGHT
    if from_ is UP:
        if currentChar == '|':
            return y + 1, x, UP
        if currentChar == 'L':
            return y, x + 1, LEFT
        if currentChar == 'J':
            return y, x - 1, RIGHT
    if from_ is LEFT:
        if currentChar == '-':
            return y, x + 1, LEFT
        if currentChar == 'J':
            return y - 1, x, DOWN
        if currentChar == '7':
            return y + 1, x, UP
    if from_ is RIGHT:
        if currentChar == '-':
            return y, x - 1, RIGHT
        if currentChar == 'F':
            return y + 1, x, UP
        if currentChar == 'L':
            return y - 1, x, DOWN

def getAnimalCoords():
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'S':
                return i, j

def changeUpOrDown(character, dir):
    if character in ['F', '7'] and dir in [RIGHT, LEFT]:
        return -1
    if character in ['F', '7'] and dir == DOWN:
        return 1
    if character in ['J', 'L'] and dir in [RIGHT, LEFT]:
        return 1
    if character in ['J', 'L'] and dir == UP:
        return -1
    if character == '|' and dir == UP:
        return -2
    if character == '|' and dir == DOWN:
        return 2
    else:
        return 0


y0, x0 = getAnimalCoords()
replace, from_ = changeS(y0, x0)
lines[y0] = lines[y0][:x0] + replace + lines[y0][x0+1:]

y, x, from_ = move(y0, x0, from_)
map[y][x] = changeUpOrDown(lines[y][x], from_)
counter = 1

while [y, x] != [y0, x0]:
    y, x, from_ = move(y, x, from_)
    map[y][x] = changeUpOrDown(lines[y][x], from_)
    counter += 1

counter2 = 0
for line in map:
    state = 0
    for number in line:
        state += number
        if (state == 2 or state == -2) and number == 0:
            counter2 += 1

# the clue to the second challenge is that you have to track if the pipe is going up or down, when it's down it has to
# come back up some time, the space between pipe going up and down is the space we are looking for
# when it turns (f.ex. F, from going up to going right) we can count space in this line only when the pipe turns back
# up (J). if we find -, we are still looking for a pipe. If we find a pipe going down (7), we still can't count the
# space because it turned back down and doesn't include next space

print(counter // 2)
# zad 1: 6823

print(counter2)
# zad 2: 415
