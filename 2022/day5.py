from collections import deque

stacks = [
    deque(),
    deque(),
    deque(),
    deque(),
    deque(),
    deque(),
    deque(),
    deque(),
    deque(),
]


def split_stacks(line: str):
    global stacks
    row = (
        line[1],
        line[5],
        line[9],
        line[13],
        line[17],
        line[21],
        line[25],
        line[29],
        line[33],
    )
    for i in range(9):
        if row[i] != " ":  # ignore empty stack
            stacks[i].appendleft(row[i])


def parse_instruction(line: str):
    line = line.split(" ")
    return (int(line[1]), int(line[3]), int(line[5]))


def print_stacks(stacks):
    max_height = max(len(l) for l in stacks)

    out = ""
    for i in reversed(range(max_height)):
        row = ""
        for c in range(9):
            try:
                row += "[" + stacks[c][i] + "]"
            except IndexError:
                row += " " * 3
            if c < 8:
                row += " "
        out += row + "\n"
    out += " 1   2   3   4   5   6   7   8   9 "
    print(out)


with open("2022/input_day5.txt", "r") as f:
    state = 0
    for line in f:
        line = line.rstrip("\r\n")
        if "[" not in line and state == 0:
            # Line with stack labels
            # Done building initial stacks
            # print_stacks(stacks)
            state = 1
            continue
        if not line:
            # Blank line before instructions
            state = 2
            continue
        if state == 0:
            split_stacks(line)
        elif state == 2:  # instructions
            move_count, stack1, stack2 = parse_instruction(line)
            storage = []
            ### part 1
            # for c in range(move_count):
            #     stacks[stack2 - 1].append(stacks[stack1 - 1].pop())
            for c in range(move_count):
                storage.append(stacks[stack1-1].pop())
            for c in range(move_count):
                stacks[stack2-1].append(storage.pop())

# print_stacks(stacks)
for stack in stacks:
    print(stack[-1], end="")
print()
# print("\nDONE")
