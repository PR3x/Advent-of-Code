from collections import Counter


example_input = ([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3])


def get_input() -> tuple[list[int], list[int]]:
    ret = ([], [])
    with open('day1.txt', 'r') as f:
        for line in f:
            a, b = line.split()
            ret[0].append(int(a))
            ret[1].append(int(b))
    return ret


def part1():
    a, b = get_input()
    a.sort()
    b.sort()
    ret = 0
    for i in range(len(a)):
        ret += abs(a[i] - b[i])
    print(ret)

def part2():
    a, b = get_input()
    b = Counter(b)
    ret = 0
    for i in a:
        ret += i * b[i]
    print(ret)


if __name__ == "__main__":
    # part1()
    part2()
