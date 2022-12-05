points = 0

def match1(in1, in2):
    ret = 0
    if in2 == 'X':
        ret += 1
        if (in1 == 'A'):
            ret += 3
        elif in1 == 'B':
            ret += 0
        elif in1 == 'C':
            ret += 6
        else:
            return -1
    elif in2 == 'Y':
        ret += 2
        if (in1 == 'A'):
            ret += 6
        elif in1 == 'B':
            ret += 3
        elif in1 == 'C':
            ret += 0
        else:
            return -1
    elif in2 == 'Z':
        ret += 3
        if (in1 == 'A'):
            ret += 0
        elif in1 == 'B':
            ret += 6
        elif in1 == 'C':
            ret += 3
        else:
            return -1
    else:
        return -1
    return ret

def match2(in1, in2):
    ret = 0
    if in1 == 'A':  # opponent chose rock
        if in2 == 'X': # you lose
            ret += 0 + 3
        elif in2 == 'Y': # you draw
            ret += 3 + 1
        elif in2 == 'Z': # you win
            ret += 6 + 2
        else:
            return -1
    elif in1 == 'B':  # opponent chose paper
        if in2 == 'X':
            ret += 0 + 1
        elif in2 == 'Y':
            ret += 3 + 2
        elif in2 == 'Z':
            ret += 6 + 3
        else:
            return -1
    elif in1 == 'C':  # opponent chose scissors
        if in2 == 'X':
            ret += 0 + 2
        elif in2 == 'Y':
            ret += 3 + 3
        elif in2 == 'Z':
            ret += 6 + 1
        else:
            return -1
    else:
        return -1
    return ret

with open('./2022/input_day2.txt', 'r') as f:
    for line in f:
        line = line.strip()
        points += match2(line[0], line[2])

print(points)
