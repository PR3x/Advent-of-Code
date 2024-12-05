from collections import defaultdict

tree = defaultdict(list)
tree["/"]

small_dir_total = 0
sized_nodes = set()

def dir_size(dir: str) -> int:
    global small_dir_total
    node_total = 0
    for node in tree[dir]:
        if type(node) is int:
            node_total += node
        else:
            if node not in sized_nodes:
                sized_nodes.add(node)
                node_total += dir_size(node)
    if node_total <= 100000:
        small_dir_total += node_total
    return node_total


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

    total = dir_size("/")
    print(total)
    print(small_dir_total)


if __name__ == "__main__":
    with open("2022/input_day7.txt", "rt") as f:
        instructions = f.read().splitlines()
        part1(instructions)
