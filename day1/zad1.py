
def isWord(target, line, iter):
    if not target:
        return [True, '']
    if iter == len(line):
        return [False, target]
    if line[iter] != target[0]:
        return [False, target]
    return [isWord(target[1:], line, iter+1)[0], target]

numWords = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def getCoords(line):
    first = -1
    last = -1
    for i in range(len(line)):
        element = line[i]
        if line[i].isdigit():
            last = element
            if first == -1:
                first = element
        else:
            for num in numWords:
                result = isWord(num, line, i)
                if result[0]:
                    last = str(numWords.index(result[1]) + 1)
                    if first == -1:
                        first = str(numWords.index(result[1]) + 1)
    if first == 0:
        return int(last)
    else:
        return int(first+last)



gameSum = 0
with open('data1.txt', 'r') as file:

    for line in file:
        line = line.strip()
        lineResult = getCoords(line)
        # print(lineResult)
        gameSum += lineResult
print(gameSum)