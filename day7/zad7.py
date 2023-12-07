from collections import Counter

lines = []
with open('data7.txt', 'r') as file:
    for line in file:
        hand = []
        for i in range(5):
            if line[i].isdigit():
                hand.append(int(line[i]))
            else:
                if line[i] == 'A':
                    hand.append(14)
                elif line[i] == 'K':
                    hand.append(13)
                elif line[i] == 'Q':
                    hand.append(12)
                elif line[i] == 'J':
                    hand.append(1)
                else:
                    hand.append(10)
        iter = 6
        val = ""
        while iter < len(line) and line[iter].isdigit():
            val += line[iter]
            iter += 1
        hand.append(15+int(val))
        lines.append(hand)

def rank(hand):
    number_count = Counter(hand)

    jokers = 0
    for key in number_count.keys():
        if key == 1:
            jokers += number_count[key]

    if jokers:
        number_count.pop(1)

    value = max(number_count.values())

    if jokers == 5 or jokers == 4:
        return 6 * 10 ** 10 + hand[4] + hand[3] * 100 + hand[2] * 10000 + hand[1] * 1000000 + hand[0] * 100000000
    if jokers == 3:
        if value == 2:
            return 6 * 10 ** 10 + hand[4] + hand[3] * 100 + hand[2] * 10000 + hand[1] * 1000000 + hand[0] * 100000000
        else:
            value = 4
    if jokers == 2:
        if value == 3:
            return 6 * 10 ** 10 + hand[4] + hand[3] * 100 + hand[2] * 10000 + hand[1] * 1000000 + hand[0] * 100000000
        if value == 2:
            return 5*10**10 + hand[4]+hand[3]*100 + hand[2]*10000 + hand[1]*1000000 + hand[0]* 100000000
        else:
            return 3 * 10 ** 10 + hand[4] + hand[3] * 100 + hand[2] * 10000 + hand[1] * 1000000 + hand[0] * 100000000
    if jokers == 1:
        if value == 4:
            return 6 * 10 ** 10 + hand[4] + hand[3] * 100 + hand[2] * 10000 + hand[1] * 1000000 + hand[0] * 100000000
        if value == 3:
            return 5 * 10 ** 10 + hand[4] + hand[3] * 100 + hand[2] * 10000 + hand[1] * 1000000 + hand[0] * 100000000
        if value == 2:
            # już mamy dropnięte jokers więc zostaje 2 1 1 num | 2 2 num
            if len(number_count) == 3:
                return 4 * 10 ** 10 + hand[4] + hand[3] * 100 + hand[2] * 10000 + hand[1] * 1000000 + hand[
                    0] * 100000000
            else:
                return 3 * 10 ** 10 + hand[4] + hand[3] * 100 + hand[2] * 10000 + hand[1] * 1000000 + hand[
                    0] * 100000000
        else:
            return 10**10 + hand[4]+hand[3]*100 + hand[2]*10000 + hand[1]*1000000 + hand[0]* 100000000


    # print(value, hand)
    if value == 5 or value == 4:
        return (value + 1)*10**10 + hand[4]+hand[3]*100 + hand[2]*10000 + hand[1]*1000000 + hand[0]* 100000000
    if value == 3:
        if len(number_count) == 3:
            return 4*10**10+ hand[4]+hand[3]*100 + hand[2]*10000 + hand[1]*1000000 + hand[0]* 100000000
        else:
            return 3*10**10 + hand[4]+hand[3]*100 + hand[2]*10000 + hand[1]*1000000 + hand[0]* 100000000
    if value == 2:
        if len(number_count) == 4:
            return 2*10**10 + hand[4]+hand[3]*100 + hand[2]*10000 + hand[1]*1000000 + hand[0]* 100000000
        else:
            return 10**10 + hand[4]+hand[3]*100 + hand[2]*10000 + hand[1]*1000000 + hand[0]* 100000000
    else:
        return hand[4]+hand[3]*100 + hand[2]*10000 + hand[1]*1000000 + hand[0]* 100000000

lines = sorted(lines, key=rank)
resultt = 0
for i in range(len(lines)):
    resultt += (i+1)*(lines[i][5]-15)
print(resultt)

