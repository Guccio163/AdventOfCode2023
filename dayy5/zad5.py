lines = []
with open('data5.txt', 'r') as file:
    for line in file:
        lines.append(line)
        # print(line)

seeds = [seed for seed in lines[0].split()]
seeds = seeds[1:]

# added with second ex
# newSeeds = []
# for i in range(0, len(seeds), 2):
#     for j in range(len(seeds[i+1])):
#         newSeeds.append(int(seeds[i])+j)


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


def findNum(num, categ):
    for triple in categ:
        order = num - int(triple[1])
        if 0 <= order < int(triple[2]):
            return int(triple[0]) + order
    return num


lowestLoc = 10 ** 20
# for seed in seeds:
for i in range(0, len(seeds), 2):
    print(i)
    for j in range(int(seeds[i+1])):
        newNum = int(seeds[i])+j
        for categ in categs:
            newNum = findNum(newNum, categ)
        lowestLoc = min(newNum, lowestLoc)

print(lowestLoc)
