from io import StringIO
import itertools

EXAMPLE_INPUT = StringIO("""7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""")


def get_input() -> list[list[int]]:
    reports: list[list[int]] = []
    with open("day2.txt", "r") as f: # EXAMPLE_INPUT as f:
        for line in f:
            report = [int(x) for x in line.split()]
            reports.append(report)
    return reports


def is_good(report: list[int]) -> bool:
    forward = sorted(report)
    reverse = list(reversed(forward))
    if report != forward and report != reverse:
        return False  # not all increasing or all decreasing
    for i in range(1, len(report)):
        diff = abs(report[i] - report[i-1])
        if diff == 0 or diff > 3:
            return False
    return True


def part1():
    safe_count = 0
    for report in get_input():
        if is_good(report):
            safe_count += 1
    print(safe_count)


def part2():
    safe_count = 0
    for report in get_input():
        combos = [list(x) for x in itertools.combinations(report, len(report)-1)]
        combos.extend([report])
        for combo in combos:
            if is_good(combo):
                safe_count += 1
                break
    print(safe_count)


if __name__ == "__main__":
    # part1()
    part2()
