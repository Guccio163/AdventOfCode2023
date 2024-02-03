from copy import deepcopy
from math import inf
from queue import PriorityQueue

instructions = {}
parts = []
with open('data19.txt', 'r') as file:
    flag = False
    for line in file:
        line = line.strip().split()
        if not line:
            flag = True
            continue
        if not flag:
            line = line[0].split('{')
            line[1] = line[1][:-1]
            line[1] = line[1].split(',')
            instructions[line[0]] = line[1]
        if flag:
            line = [int(element[2:]) for element in line[0][1:-1].split(',')]
            parts.append(line)
print(instructions)
print(parts)

# A = {'x':[], 'm':[], 'a':[], 's':[]}
# R = {'x':[], 'm':[], 'a':[], 's':[]}
# a is a set of sets of constraints that if a part meets, then it fits to this category
A = []
R = []

queue = []
#                   x          m          a          s
firstBounds = [[-inf, inf],[-inf, inf],[-inf, inf],[-inf, inf]]
queue.append(("in", firstBounds))
while queue:
    # print(queue)
    queueElement = queue.pop()
    currentBounds = queueElement[1]
    # print(queueElement[0])
    # print(queueElement[1])
    instr = instructions[queueElement[0]]

    # I GUESS THERE SHOULD BE ALSO AN ARRAY TO DO MIRROR WHINGS TO WHAT IM DOING, F.EX. IS I HAD a>1500 AND NOW I HAVE
    # a<1700 TO GO TO THE "xd" THEN I KNOW THAT I HAVE a>1700 TO BE IN DEFAULT CATEGORY
    # leaving it for now, interview is far more important

    for pair in instr[:-1]:
        split = pair.split(':')
        bound = split[0]
        dest = split[1]
        # print(inst)
        # set currentBounds
        if bound[0] == 'x':
            letterIndex = 0
        elif bound[0] == 'm':
            letterIndex = 1
        elif bound[0] == 'a':
            letterIndex = 2
        elif bound[0] == 's':
            letterIndex = 3
        else:
            letterIndex = 4
        # print(inst[0], inst[1])
        if bound[1] == '<':
            currentBounds[letterIndex][1] = min(int(bound[2:]), currentBounds[letterIndex][1])
            # print(int(inst[0][2:]))
        elif bound[1] == '>':
            currentBounds[letterIndex][0] = max(int(bound[2:]), currentBounds[letterIndex][0])
            # print(int(inst[0][2:]))

        flag = False
        for bounds in currentBounds:
            if bounds[0]>bounds[1]:
                flag = True
                break
        if flag:
            break

        print(currentBounds)

        if dest == 'A':
            # set A bounds based on current state (parts have to have this state to reach here)
            A.append(deepcopy(currentBounds))
            # continue
        elif dest == 'R':
            # set R bounds based on current state (parts have to have this state to reach here)
            R.append(deepcopy(currentBounds))
            # continue
        else:
            queue.append([dest, deepcopy(currentBounds)])
            # print("appended to queue ", inst[1])


    if instr[-1] == 'A':
        # set A bounds based on current state (parts have to have this state to reach here)
        A.append(deepcopy(currentBounds))
    elif instr[-1] == 'R':
        # set R bounds based on current state (parts have to have this state to reach here)
        R.append(deepcopy(currentBounds))
    else:
        queue.append([instr[-1], deepcopy(currentBounds)])
print(A)
print(R)

# for part in parts:
#     for


