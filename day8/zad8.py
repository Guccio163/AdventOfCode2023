lines = {}
preLines = []
with open('data8.txt', 'r') as file:
    for line in file:
        preLines.append(line)

directions = preLines[0][:-1]

for line in preLines[2:]:
    loc = line[:3]
    left = line[7:10]
    right = line[12:15]
    lines[loc] = [left, right]

def getLoc(loc):
    for direction in directions:
        if direction == 'L':
            loc = lines[loc][0]
        elif direction == 'R':
            loc = lines[loc][1]
    return loc

def answer1():
    loc = "AAA"
    steps = 0
    while loc != "ZZZ":
        loc = getLoc(loc)
        steps += 1
    print(steps*len(directions))

def nwm(a, b):
    while b:
        a, b = b, a % b
    return a

def nww(a, b):
    return a * b // nwm(a, b)

def answer2():
    locs = []
    for key in lines.keys():
        if key[2] == "A":
            locs.append(key)

    locssteps = []
    for loc in locs:
        steps = 0
        while loc[2] != "Z":
            loc = getLoc(loc)
            steps += 1
        locssteps.append(steps)

    current_nww = 1
    for step in locssteps:
        current_nww = nww(current_nww, step)

    print(current_nww *len(directions))

answer1() # 20569
answer2() # 21366921060721