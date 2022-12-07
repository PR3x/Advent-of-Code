from collections import defaultdict

tree = defaultdict(list)
tree["/"]


def part1(instructions: list[str]):
    stack = ["/"]  # current directory is last element
    for line in instructions:
        line = line.split()
        if line[0] == "$":
            # this is a command
            if line[1] == "cd":
                if line[2] == "..":
                    stack.pop()
                else:
                    stack.append(line[2])
            # ignore ls (the only other command)
        else:
            # printing directory
            if line[0] == "dir":
                # subdirectory
                tree[stack[-1]].append(line[1])
                tree[line[1]]  # ensure key exists
            else:
                # file
                # we don't care about its name, just its size
                tree[stack[-1]].append(int(line[0]))
    
    total = 0
    for dir in tree.values():
        dir_total = 0
        for val in dir:
            if type(val) is int:
                dir_total += val
        if dir_total <= 100000:
            total += dir_total
    print(total)


if __name__ == "__main__":
    with open("2022/input_day7.txt", "rt") as f:
        instructions = f.read().splitlines()
        part1(instructions)
