instructions = []
with open('data15.txt', 'r') as file:
    for line in file:
        line = line.strip().split()[0]
        instructions = line.split(',')


def customHash(letters):
    hashed = 0
    for letter in letters:
        hashed = ((hashed + ord(letter)) * 17) % 256
    return hashed


# FIRST PART OF THE TASK
# print(sum([customHash(instr) for instr in instructions]))
# right answer 503154

boxes = [{} for _ in range(256)]
for instr in instructions:
    temp = instr.split('=')
    if len(temp) == 1:
        temp = temp[0][:-1]
        boxNum = customHash(temp)
        if hash(temp) in boxes[boxNum].keys():
            boxes[boxNum].pop(hash(temp))
    else:
        letters = temp[0]
        num = int(temp[1])
        boxes[customHash(letters)][hash(letters)] = num

bigSum = 0
for i, box in enumerate(boxes):
    for j, key in enumerate(box.keys()):
        bigSum += (i + 1) * (j+1) * box[key]
print(bigSum)

# or I could just write:
print(sum([(i + 1) * (j+1) * box[key] for i, box in enumerate(boxes) for j, key in enumerate(box.keys())]))
# but in my opinion, the first one is still more readable
# either way right answer 251353
