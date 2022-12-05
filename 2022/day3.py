def to_priority(item: str):
    val = ord(item) - 96
    if val < 0:
        val += 58
    return val


def part1_shared(line: str):
    half = len(line) // 2
    sack1 = line[0:half]
    sack2 = line[half:]
    shared = set(sack1).intersection(sack2)
    return shared


total = 0

with open("2022/input_day3.txt", "r") as f:
    group = []
    for line in f:
        ### part 1
        # sack_total = 0
        line = line.strip()
        # shared = part1_shared(line)
        # for item in shared:
        #     sack_total += to_priority(item)
        # total += sack_total
        group.append(line)
        if len(group) >= 3:
            shared = set(group[0]).intersection(group[1]).intersection(group[2])
            total += to_priority(shared.pop())
            group = []

print(total)
