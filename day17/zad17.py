from enum import Enum
from math import inf

lines = []
with open('data17.txt', 'r') as file:
    for line in file:
        line = line.strip().split()[0]
        lines.append(line)
        # print(line)

class Directions(Enum):
    NORTH = 2
    EAST = 3
    SOUTH = 5
    WEST = 7


NORTH = Directions.NORTH
EAST = Directions.EAST
SOUTH = Directions.SOUTH
WEST = Directions.WEST
        
width = len(lines[0])
height = len(lines)

def getCost(lines, i, j, dir, k):
    if i == len(lines)-1 and j==len(lines[0])-1:
        return int(lines[i][j])
    fullSet = [NORTH, EAST, SOUTH, WEST]
    toRemove = []
    if i == 0:
        toRemove.append(NORTH)
    if i == len(lines)-1:
        toRemove.append(SOUTH)
    if j == 0:
        toRemove.append(WEST)
    if j == len(lines[0])-1:
        toRemove.append(EAST)
    if k == 3:
        toRemove.append(dir)
    if dir == NORTH:
        toRemove.append(SOUTH)
    if dir == EAST:
        toRemove.append(WEST)
    if dir == SOUTH:
        toRemove.append(NORTH)
    if dir == WEST:
        toRemove.append(EAST)
    toRemove.append(dir)

    # fullSet = [filter(lambda x: x not in toRemove, fullSet)]

    fullSet = [item for item in fullSet if item not in toRemove]

    minimumCost = inf
    for item in fullSet:
        print(item.value)
    for dirr in fullSet:
        if dirr is not dir:
            newk = 1
        else:
            newk = k+1
        if dirr is NORTH:
            minimumCost = min(minimumCost, getCost(lines, i-1, j, NORTH, newk))
        if dirr is EAST:
            minimumCost = min(minimumCost, getCost(lines, i, j+1, EAST, newk))
        if dirr is SOUTH:
            minimumCost = min(minimumCost, getCost(lines, i+1, j, SOUTH, newk))
        if dirr is WEST:
            minimumCost = min(minimumCost, getCost(lines, i, j-1, WEST, newk))
    return minimumCost + int(lines[i][j])

print(getCost(lines, 0, 0, SOUTH, 0))
