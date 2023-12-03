lines = []
with open('data3.txt', 'r') as file:
    for line in file:
        lines.append(line)

# second solution: find every star and count her adjacent, if 2 figure out the numbers

finalSum = 0

def getNumLeft(i, j, current=""):
    if j == -1:
        return current
    if not lines[i][j].isdigit():
        return current
    return getNumLeft(i, j-1, lines[i][j]+current)
def getNumRight(i, j, current=""):
    if j == len(lines):
        return current
    if not lines[i][j].isdigit():
        return current
    return getNumRight(i, j + 1, current + lines[i][j])
def getNum(i, j):
    return getNumLeft(i, j) + getNumRight(i, j+1)

def findNums(i, j):
    nums = ['.' for _ in range(8)]
    lastIndex = len(lines)-1
    result = []

    if i != 0 and j != 0:
        nums[0] = lines[i-1][j-1]
    if i != 0:
        nums[1] = lines[i-1][j]
    if i != 0 and j != lastIndex:
        nums[2] = lines[i-1][j+1]
    if j != 0:
        nums[3] = lines[i][j-1]
    if j != lastIndex:
        nums[4] = lines[i][j+1]
    if i != lastIndex and j != 0:
        nums[5] = lines[i+1][j-1]
    if i != lastIndex:
        nums[6] = lines[i+1][j]
    if i != lastIndex and j != lastIndex:
        nums[7] = lines[i+1][j+1]

    if nums[0].isdigit():
        result.append(getNum(i-1, j-1))
        if nums[2].isdigit() and not nums[1].isdigit():
            result.append(getNum(i-1, j+1))
    else:
        if nums[1].isdigit():
            result.append(getNum(i-1, j))
        elif nums[2].isdigit():
            result.append((getNum(i-1, j+1)))

    if nums[3].isdigit():
        result.append(getNum(i, j-1))
    if nums[4].isdigit():
        result.append(getNum(i, j+1))
    if nums[5].isdigit():
        result.append(getNum(i+1, j-1))
        if nums[7].isdigit() and not nums[6].isdigit():
            result.append(getNum(i+1, j+1))
    else:
        if nums[6].isdigit():
            result.append(getNum(i+1, j))
        elif nums[7].isdigit():
            result.append((getNum(i+1, j+1)))

    return result

for i in range(len(lines)):
    line = lines[i]
    for j in range(len(line)):
        digit = line[j]
        if digit == '*':
            nums = findNums(i, j)
            if len(nums) == 2:
                finalSum += int(nums[0]) * int(nums[1])

print(finalSum)