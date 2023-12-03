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

def isPossible(line, gameNum):
    game = line.strip().replace(':', ';').split(";")
    draws = game[1:]
    for draw in draws:
        pairs = draw.strip().split(",")
        for pair in pairs:
            pair = pair.strip().split()
            number = pair[0].strip()
            name = pair[1].strip()
            if int(number) > getNum(name):
                print(str(gameNum)+" impossible, tried to draw" + str(pair))
                return False
    return True

gameNum = 0
with open('data2.txt', 'r') as file:

    for line in file:
        gameNum += 1
        if isPossible(line, gameNum):
            trueSum += gameNum
    print("Truesum:" + str(trueSum))
        # lines.append(tokens)