lines = []
with open('data9.txt', 'r') as file:
    for line in file:
        line = line.strip().split()
        lines.append([int(element) for element in line])

def extrapolateBackward(firstNums):
    firstNums.reverse()
    currentExtr = 0
    for num in firstNums:
        currentExtr = num-currentExtr
        print(currentExtr)
    return currentExtr

extrapolatedSum = 0
for line in lines:
    currentLine = line
    nextLine = []
    # zad 1
    # lastNums = [line[-1]]
    #zad 2
    lastNums = [line[0]]
    shouldExtr = False
    while not shouldExtr:
        for i in range(1, len(currentLine)):
            nextLine.append(currentLine[i]-currentLine[i-1])
        shouldExtr = all(element == 0 for element in nextLine)
        currentLine = nextLine
        nextLine = []
        #zad 1
        # lastNums.append(currentLine[-1])
        #zad 2
        lastNums.append(currentLine[0])
    # zad 1
    # extrapolatedSum += sum(lastNums)
    # zad 2
    extrapolatedSum += extrapolateBackward(lastNums)

print(extrapolatedSum)
# zad 1: 1637452029
# zad 2: 908
