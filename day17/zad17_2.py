from math import inf
from queue import PriorityQueue

lines = []
with open('xd.txt', 'r') as file:
    for line in file:
        line = line.strip().split()[0]
        lines.append(line)
        # print(line)
height = len(lines)-1
width = len(lines[0])-1

def getSteps(i, j):
    if i == 0:
        if j == 0:
            return ((0, 1), (1, 0))
        elif j == width:
            return ((0, -1), (1, 0))
        return ((0, 1), (0, -1), (1, 0))
    elif i == height:
        if j == 0:
            return ((0, 1), (-1, 0))
        elif j == width:
            return ((0, -1), (-1, 0))
        return ((0, 1), (0, -1), (-1, 0))
    elif j == 0:
        return ((0, 1), (1, 0), (-1, 0))
    elif j == width:
        return ((0, -1), (1, 0), (-1, 0))
    return ((0, 1), (0, -1), (1, 0), (-1, 0))

def are3inRow(i, j, step):
    if i-step[0] > height or j- step[1] > width or i-2*step[0] > height or j-2*step[1] > width:
        return False
    if steps[i][j] == steps[i-step[0]][j-step[1]] == steps[i-2*step[0]][j-2*step[1]] == step:
        return True


d = [[inf for _ in lines[0]] for _ in lines]
d[0][0] = 0

steps = [[(height+1, width+1) for _ in lines[0]]for _ in lines]
steps[0][0] = (0,1)

queue = PriorityQueue()
for i in range(len(lines)):
    for j in range(len(lines[0])):
        queue.put((inf, i, j))
queue.put((0, 0, 0))

while not queue.empty():
    vortex = queue.get()
    i, j = vortex[1], vortex[2]
    for step in getSteps(i, j):
        print(i, j, step)
        if d[i+step[0]][j+step[1]] > d[i][j] + int(lines[i+step[0]][j+step[1]]) and not are3inRow(i, j, step):
            d[i + step[0]][j + step[1]] = d[i][j] + int(lines[i + step[0]][j + step[1]])
            steps[i + step[0]][j + step[1]] = step
            queue.put((d[i + step[0]][j + step[1]], i + step[0], j + step[1] ))
        elif are3inRow(i, j, step):
            print("there are 3 in row ", i, j, step)
print(d[height][width])

def convertSteps(step):
    if step == (0, 1):
        return ">"
    if step == (0, -1):
        return "<"
    if step == (1, 0):
        return "v"
    if step == (-1, 0):
        return "^"
    return "-"
# dupa = [convertSteps(step) for line in steps for step in line]
for line in steps:
    print([convertSteps(step) for step in line])

for line in d:
    print(line)

cur = [height, width]
while cur != [0,0]:
    print(cur, d[cur[0]][cur[1]])
    cur = [cur[0]-steps[cur[0]][cur[1]][0], cur[1]-steps[cur[0]][cur[1]][1]]