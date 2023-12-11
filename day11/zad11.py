lines = []
with open('data11.txt', 'r') as file:
    for line in file:
        line = line.strip().split()[0]
        lines.append(line)

hashList = [[r, c] for c in range(len(lines[0])) for r in range(len(lines)) if lines[r][c] == '#']
rows1 = [r for r in range(len(lines)) if r not in [r for [r, c] in hashList]]
cols1 = [c for c in range(len(lines[0])) if c not in [c for [r, c] in hashList]]

def distance(first, second, expand):
    higherX = max(first[1], second[1])
    lowerX = min(first[1], second[1])
    higherY = max(first[0], second[0])
    lowerY = min(first[0], second[0])
    bias = 0
    for row in rows1:
        if lowerY < row < higherY:
            bias += expand - 1
    for column in cols1:
        if lowerX < column < higherX:
            bias += expand - 1
    return higherY - lowerY + higherX - lowerX + bias

def getAllDistances(expand=2):
    return sum(
        [distance(hashList[i], hashList[j], expand) for i in range(len(hashList)) for j in range(i + 1, len(hashList))])

print(getAllDistances())
print(getAllDistances(1000000))

# zad1: 9509330
# zad2: 635832237682
