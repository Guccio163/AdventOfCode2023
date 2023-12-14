lines = []
with open('data14.txt', 'r') as file:
    for line in file:
        line = line.strip().split()[0]
        lines.append(line)
        print(line)

def getLoad(hash, rocks):
    summ = 0
    for i in range(hash-1, hash-rocks-1, -1):
        summ += i
    return summ

height = len(lines)
totalSum = 0
for i in range(len(lines[0])):
    lastHash = height+1
    rocks = 0
    for j in range(height):
        if lines[j][i] == 'O':
            rocks += 1
        if lines[j][i] == '#':
            totalSum += getLoad(lastHash, rocks)
            rocks = 0
            lastHash = height-j
    totalSum += getLoad(lastHash, rocks)
print(totalSum)

# zad1 109654
