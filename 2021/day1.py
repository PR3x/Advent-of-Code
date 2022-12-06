#!/usr/bin/env python


def part1():
    out = 0
    prev = -1
    with open("day1.txt", "r") as f:
        for scan in f:
            scan = int(scan)
            if prev == -1:
                pass
            elif prev < scan:
                out += 1
            prev = scan

    print(out)


def part2():
    out: int = 0
    a: int = -1
    b: int = -1
    c: int = -1
    total: int = -1

    with open("day1.txt", "r") as f:
        for scan in f:
            scan = int(scan)
            if a == -1:
                a = scan
            elif b == -1:
                b = scan
            elif c == -1:
                c = scan
                total = a + b + c
            else:
                a = b
                b = c
                c = scan
                if a + b + c > total:
                    out += 1
                total = a + b + c
    print(out)


if __name__ == "__main__":
    part1()
    part2()
