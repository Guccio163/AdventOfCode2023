lines = []
with open('data5.txt', 'r') as file:
    for line in file:
        lines.append(line)

seeds = [seed for seed in lines[0].split()]
seeds = seeds[1:]

changeCateg = False
categNum = 0
categs = [[]]
for line in lines[2:]:
    if line[0] == '\n':
        categs.append([])
        categNum += 1
        continue
    if line[0].isdigit():
        categs[categNum].append(line[:-1].split())

seedIntervals = []
for i in range(0, len(seeds), 2):
    seedIntervals.append([int(seeds[i]), int(seeds[i])+int(seeds[i+1])])
seedIntervals.sort()

seedIntervalsLength = len(seedIntervals)
seedIntervalsDown = [SI for SI in seedIntervals]

mappingUp = []
mappingDown = []

nextTurnSeedIntervals = []
nextTurnSeedIntervalsDown = []

# dla każdego interwału sprawdź gdzie się mieści początek i jak całość się mieści to przekształć
# jak tylko początek sie mieści to początek przekształcasz, wysplitowaną góre appendujesz do nextTurn i przekształcasz
# kolejną część dołu, przekształcenie to split góry i append nowego przekształconego dołu do nowej tablicy
# tak dla każdego przedziału aż do końca
# na sam koniec nowe przypisane przedziały stają się seedIntervalsDown
def mapDown(seedIntervalDown, seedInterval):
    interval = seedIntervalDown
    # print(seedIntervalDown, seedInterval)
    for i in range(len(mappingUp)):
        mapInterval = mappingUp[i]
        if mapInterval[0] <= interval[0] <= mapInterval[1] and mapInterval[0] <= interval[1] <= mapInterval[1]:
            nextTurnSeedIntervals.append(seedInterval)
            bias = interval[0] - mapInterval[0]
            nextTurnSeedIntervalsDown.append([mappingDown[i][0]+bias, mappingDown[i][0]+bias+interval[1]-interval[0]])
            return
        elif mapInterval[0] < interval[0] < mapInterval[1]:
            pieceFitting = mapInterval[1]-interval[0]+1
            nextTurnSeedIntervals.append([seedInterval[0], seedInterval[0]+pieceFitting-1])
            bias = interval[0] - mapInterval[0]
            nextTurnSeedIntervalsDown.append([mappingDown[i][0]+bias, mappingDown[i][0]+bias+pieceFitting-1])
            mapDown([seedIntervalDown[0]+pieceFitting,seedIntervalDown[1]], [seedInterval[0] + pieceFitting, seedInterval[1]])
            return

for categ in categs:
    upTemp = []
    downTemp = []
    for i in range(len(categ)):
        row = categ[i]
        upTemp.append([int(row[1]), int(row[1])+int(row[2])-1, int(row[0])])
    upTemp.sort()
    for interval in upTemp:
        downTemp.append([interval[2], interval[2]+interval[1]-interval[0]])
    mappingUp = []
    mappingDown = []
    if upTemp[0][0] != 0:
        mappingUp.append([0, upTemp[0][0]-1])
        mappingDown.append([0, upTemp[0][0]-1])
    for i in range(len(upTemp)-1):
        mappingUp.append(upTemp[i][:2])
        mappingDown.append(downTemp[i])
        if upTemp[i][1]+1 != upTemp[i+1][0]:
            mappingUp.append([upTemp[i][1]+1, upTemp[i+1][0]-1])
            mappingDown.append([upTemp[i][1]+1, upTemp[i+1][0]-1])
    mappingUp.append([upTemp[-1][0], upTemp[-1][1]])
    mappingDown.append(downTemp[-1])
    mappingUp.append([upTemp[-1][1]+1, 10**20])
    mappingDown.append([upTemp[-1][1]+1, 10**20])

    for i in range(len(seedIntervalsDown)):
        mapDown(seedIntervalsDown[i], seedIntervals[i])

    print(seedIntervals)
    print(seedIntervalsDown)
    print()

    seedIntervals = nextTurnSeedIntervals
    seedIntervalsDown = nextTurnSeedIntervalsDown
    nextTurnSeedIntervals = []
    nextTurnSeedIntervalsDown = []

print(seedIntervals)
print(seedIntervalsDown)
print()


lowestLoc = 10**20
for interval in seedIntervalsDown:
    lowestLoc = min(interval[0], lowestLoc)
print(lowestLoc)
