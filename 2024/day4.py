import numpy as np
from io import StringIO

EXAMPLE_INPUT = StringIO("""MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""")


def get_input():
    with EXAMPLE_INPUT as f: # open("day4.txt", "r") as f:
        data = f.read().splitlines()
    return np.array([list(line) for line in data], str)


def part1():
    ret = 0
    data = get_input()
    for x in range(4):
        for line in data:
            print(line)
            for i, char in enumerate(line):
                if (
                    char == "X"
                    and i < len(line) - 3
                    and line[i + 1] == "M"
                    and line[i + 2] == "A"
                    and line[i + 3] == "S"
                ):
                    ret += 1
                    print(f"XMAS: {i}")
                elif (
                    char == "X"
                    and line[i - 1] == "M"
                    and line[i - 2] == "A"
                    and line[i - 3] == "S"
                ):
                    ret += 1
                    print(f"SAMX: {i}")
        data = np.rot90(data)
        print(f"ROTATED {90*x}\n")
    print("Total:", ret)


def part2():
    pass


if __name__ == "__main__":
    part1()
    # part2()
