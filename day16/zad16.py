from enum import Enum

lines = []
with open('data16.txt', 'r') as file:
    for line in file:
        line = line.strip().split()[0]
        lines.append(line)
width = len(lines[0])
height = len(lines)


class Directions(Enum):
    RIGHT = 2
    DOWN = 3
    LEFT = 5
    UP = 7


RIGHT = Directions.RIGHT
DOWN = Directions.DOWN
LEFT = Directions.LEFT
UP = Directions.UP


# if light goes through a tile rightward multiply by 2, down:3, left:5, up:7

# first approach, more straightforward but recursion exceeded limits
# def markTheTiles(coords, direction):
#     if not (0 <= coords[1] < len(lines[0]) and 0 <= coords[0] < len(lines)):
#         return
#
#     if beamsArr[coords[0]][coords[1]] % direction.value == 0:
#         return
#     beamsArr[coords[0]][coords[1]] *= direction.value
#
#     if lines[coords[0]][coords[1]] == '|' and (direction == RIGHT or direction == LEFT):
#         markTheTiles([coords[0] - 1, coords[1]], UP)
#         markTheTiles([coords[0] + 1, coords[1]], DOWN)
#     elif lines[coords[0]][coords[1]] == '-' and (direction == UP or direction == DOWN):
#         markTheTiles([coords[0], coords[1] + 1], RIGHT)
#         markTheTiles([coords[0], coords[1] - 1], LEFT)
#     elif lines[coords[0]][coords[1]] == '\\':
#         if direction == RIGHT:
#             markTheTiles([coords[0] + 1, coords[1]], DOWN)
#         if direction == DOWN:
#             markTheTiles([coords[0], coords[1] + 1], RIGHT)
#         if direction == LEFT:
#             markTheTiles([coords[0] - 1, coords[1]], UP)
#         if direction == UP:
#             markTheTiles([coords[0], coords[1] - 1], LEFT)
#     elif lines[coords[0]][coords[1]] == '/':
#         if direction == RIGHT:
#             markTheTiles([coords[0] - 1, coords[1]], UP)
#         if direction == DOWN:
#             markTheTiles([coords[0], coords[1] - 1], LEFT)
#         if direction == LEFT:
#             markTheTiles([coords[0] + 1, coords[1]], DOWN)
#         if direction == UP:
#             markTheTiles([coords[0], coords[1] + 1], RIGHT)
#     else:
#         if direction == RIGHT:
#             markTheTiles([coords[0], coords[1] + 1], RIGHT)
#         elif direction == DOWN:
#             markTheTiles([coords[0] + 1, coords[1]], DOWN)
#         elif direction == LEFT:
#             markTheTiles([coords[0], coords[1] - 1], LEFT)
#         elif direction == UP:
#             markTheTiles([coords[0] - 1, coords[1]], UP)
#         else:
#             print("shouldn't happen")


def nextDirections(coords, direction, beamsArr):
    r = coords[0]
    c = coords[1]

    if not (0 <= c < width and 0 <= r < height) or beamsArr[r][c] % direction.value == 0:
        return [-1]

    beamsArr[r][c] *= direction.value

    if lines[r][c] == '|' and (direction in [RIGHT, LEFT]):
        return 2, ([r-1, c], UP), ([r+1, c], DOWN)
    elif lines[r][c] == '-' and (direction in [UP, DOWN]):
        return 2, ([r, c+1], RIGHT), ([r, c-1], LEFT)
    elif lines[r][c] == '\\':
        if direction == RIGHT:
            return [r + 1, c], DOWN
        if direction == DOWN:
            return [r, c+1], RIGHT
        if direction == LEFT:
            return [r-1, c], UP
        if direction == UP:
            return [r, c-1], LEFT
    elif lines[r][c] == '/':
        if direction == RIGHT:
            return [r-1, c], UP
        if direction == DOWN:
            return [r, c-1], LEFT
        if direction == LEFT:
            return [r+1, c], DOWN
        if direction == UP:
            return [r, c+1], RIGHT
    else:
        if direction == RIGHT:
            return [r, c+1], RIGHT
        elif direction == DOWN:
            return [r+1, c], DOWN
        elif direction == LEFT:
            return [r, c-1], LEFT
        else:
            return [r-1, c], UP

def findBiggestSum(i, j, startDir):
    beamsArr = [[1 for _ in lines[0]] for _ in lines]
    start = [i, j]
    toDo = [(start, startDir)]

    while (toDo):
        task = toDo.pop()
        result = nextDirections(task[0], task[1], beamsArr)
        if result[0] == -1:
            continue
        if result[0] == 2:
            toDo.append(result[1])
            toDo.append(result[2])
        else:
            toDo.append(result)

    bigSum = sum([1 for row in beamsArr for element in row if element != 1])
    return bigSum


reallyBigSum = 0
for j in [0, len(lines[0]) - 1]:
    startDir = LEFT
    if j == 0:
        startDir = RIGHT
    for i in range(len(lines)):
        reallyBigSum = max(reallyBigSum, findBiggestSum(i, j, startDir))

for j in [0, len(lines) - 1]:
    startDir = UP
    if j == 0:
        startDir = DOWN
    for i in range(len(lines[0])):
        reallyBigSum = max(reallyBigSum, findBiggestSum(j, i, startDir))

print(reallyBigSum)

# first: 7242
# second: 7572
