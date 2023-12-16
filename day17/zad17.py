lines = []
with open('data17.txt', 'r') as file:
    for line in file:
        line = line.strip().split()[0]
        lines.append(line)
        print(line)
        
width = len(lines[0])
height = len(lines)