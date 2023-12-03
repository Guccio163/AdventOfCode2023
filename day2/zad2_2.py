lines = []
red = 12
green = 13
blue = 14
trueSum = 0
def getNum(name):
    if name == "red":
        return 12
    elif name == "green":
        return 13
    elif name == "blue":
        return 14
    else:
        return 0

def getIndex(name):
    if name == "red":
        return 0
    elif name == "green":
        return 1
    elif name == "blue":
        return 2
    else:
        return 3

def lowestPossible(line, gameNum):
    game = line.strip().replace(':', ';').split(";")
    # red / green / blue
    colorMins = [0,0,0]
    draws = game[1:]
    for draw in draws:
        pairs = draw.strip().split(",")
        for pair in pairs:
            pair = pair.strip().split()
            number = pair[0].strip()
            name = pair[1].strip()
            if int(number) > colorMins[getIndex(name)]:
                colorMins[getIndex(name)] = int(number)
    return colorMins[0]*colorMins[1]*colorMins[2]

gameNum = 0
with open('data2.txt', 'r') as file:

    for line in file:
        gameNum += 1
        trueSum += lowestPossible(line, gameNum)
    print("Truesum:" + str(trueSum))
        # lines.append(tokens)