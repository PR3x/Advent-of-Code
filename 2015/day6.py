from itertools import chain
from collections import Counter

lights = [[False] * 10] * 10


def part1(line: str):
    tokens = line.split()
    if tokens[0] == "toggle":
        startx, starty = map(int, tokens[1].split(","))
        endx, endy = map(int, tokens[3].split(","))
        for y in range(starty, endy + 1):
            for x in range(startx, endx + 1):
                print(x, y)
                lights[y][x] = not lights[y][x]
    elif tokens[0] == "turn":
        startx, starty = map(int, tokens[2].split(","))
        endx, endy = map(int, tokens[4].split(","))
        if tokens[1] == "on":
            for y in range(starty, endy + 1):
                for x in range(startx, endx):
                    lights[y][x] = True
        elif tokens[1] == "off":
            for y in range(starty, endy + 1):
                for x in range(startx, endx):
                    lights[y][x] = False


def printlights():
    for row in lights:
        print(row)


if __name__ == "__main__":
    with open("2015/input_day6.txt", "r") as f:
        for line in f:
            part1(line.rstrip())

    print(Counter(i for i in list(chain.from_iterable(lights)))[True])
