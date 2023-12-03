lines = []
with open('data3.txt', 'r') as file:
    for line in file:
        lines.append(line)

specialChars = []

def checkTiles(array, i, j):
    for move in array:
        if not lines[i + move[0]][j + move[1]].isalnum() and lines[i + move[0]][j + move[1]] != '.':
            print("character found at " + str(i) + " " + str(j) + ": " + lines[i + move[0]][j + move[1]])
            specialChar = lines[i + move[0]][j + move[1]]
            if not (specialChar == '*' or specialChars == '=' or specialChar == '%' or specialChar == '-' or specialChar == '&' or specialChar == '$' or specialChar == '#' or specialChar == '/' or specialChar == '+' or specialChar == '=' or specialChar == '@'):
                specialChars.append([lines[i + move[0]][j + move[1]], i])
            return True
    return False


def checkForFlags(i, j):
    if i == 0:
        if j == 0:
            return checkTiles([[0, 1], [1, 0], [1, 1]], i, j)
        if j == len(lines[i]) - 1:
            return checkTiles([[0, -1], [1, -1], [1, 0]], i, j)
        else:
            return checkTiles([[0, -1], [0, 1], [1, -1], [1, 0], [1, 1]], i, j)

    if i == len(lines) - 1:
        if j == 0:
            return checkTiles([[-1, 0], [-1, 1], [0, 1]], i, j)
        if j == len(lines[i]) - 1:
            return checkTiles([[-1, -1], [-1, 0], [0, -1], ], i, j)
        else:
            return checkTiles([[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1]], i, j)
    if j == 0:
        return checkTiles([[-1, 0], [-1, 1], [0, 1], [1, 0], [1, 1]], i, j)
    if j == len(lines[i]) - 1:
        return checkTiles([[-1, -1], [-1, 0], [0, -1], [1, -1], [1, 0]], i, j)

    return checkTiles([[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]], i, j)


finalSum = 0

for i in range(len(lines)):
    line = lines[i]
    num = ""
    flag = False
    for j in range(len(line)):
        digit = line[j]
        if digit.isdigit():
            num += digit
            if not flag:
                flag = checkForFlags(i, j)
        else:
            if num != "" and flag == True:
                finalSum += int(num)
                print(num)
                print(finalSum)
            num = ""
            flag = False
print(finalSum)
print(specialChars)