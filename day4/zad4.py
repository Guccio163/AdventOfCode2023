lines = []
with open('data4.txt', 'r') as file:
    for line in file:
        lines.append(line)

cardCount = [1 for _ in lines]

def getMoreCards(index, wonCount):
    multiplier = cardCount[index]
    spaceToEnd = len(cardCount)-index-1
    spaceToFill = min(spaceToEnd, wonCount)
    for i in range(spaceToFill):
        cardCount[index+1+i] += multiplier

resultSum = 0
for i in range(len(lines)):
    line = lines[i].strip().split()
    winningNums = []
    flag = False
    win = 0
    # win = 0.5
    for word in line:
        if word == '|':
            flag = True
            continue
        if flag:
            if word in winningNums:
                win += 1
                # win *= 2
        else:
            winningNums.append(word)
    # if win != 0.5:
    #     resultSum += win
    getMoreCards(i, win)
# print(resultSum)
print(sum(cardCount))

