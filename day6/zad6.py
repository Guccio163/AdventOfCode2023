lines = []
with open('data6.txt', 'r') as file:
    for line in file:
        lines.append(line)
time = lines[0].split()[1:]
distance = lines[1].split()[1:]

# pretty straight-forward, could be a binary search if it took too long
returnTimes = []
for i in range(len(time)):
    t = int(time[i])
    for j in range(1,t):
        if j*(t-j) > int(distance[i]):
            returnTimes.append(t-2*j+1)
            break

bigTime = ""
for t in time:
    bigTime += t
bigTime = int(bigTime)

bigDistance = ""
for d in distance:
    bigDistance += d
bigDistance = int(bigDistance)

for j in range(1, bigTime):
    if j * (bigTime - j) > bigDistance:
        print(bigTime - 2 * j + 1)
        break

result = 1
for ti in returnTimes:
    result *= ti
# print(result)