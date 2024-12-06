import re
from io import StringIO

EXAMPLE_INPUT = StringIO(
    """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
)


def get_input() -> str:
    with open("day3.txt", "r") as f:  # EXAMPLE_INPUT as f:
        return f.read().strip()


def part1():
    total = 0
    f = get_input()
    regex = re.compile(r"(?<=mul\()(\d+,\d+)(?=\))", re.M)
    for match in regex.findall(f):
        x, y = match.split(",")
        total += int(x) * int(y)
    print(total)


def part2():
    total = 0
    f = get_input()
    enable = True
    regex = re.compile(r"(?<=mul\()(\d+,\d+)(?=\))|(do(?:n't)*\(\))")
    for match in regex.findall(f):
        if match[0] and enable:
            x, y = match[0].split(",")
            total += int(x) * int(y)
        elif match[1]:
            if match[1] == "do()":
                enable = True
            elif match[1] == "don't()":
                enable = False
    print(total)


if __name__ == "__main__":
    # part1()
    part2()
