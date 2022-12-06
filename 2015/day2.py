total_paper = 0
total_ribbon = 0


def paper(line: str) -> int:
    l, w, h = map(int, line.split("x"))
    s1 = l * w
    s2 = w * h
    s3 = h * l
    slack = min(s1, s2, s3)
    return 2 * s1 + 2 * s2 + 2 * s3 + slack


def ribbon(line: str) -> int:
    l, w, h = map(int, line.split("x"))
    side1, side2, _ = sorted((l, w, h))
    perimeter = 2 * side1 + 2 * side2
    volume = l * w * h
    return perimeter + volume


with open("2015/input_day2.txt", "rt") as f:
    for line in f:
        line = line.rstrip()
        total_paper += paper(line)
        total_ribbon += ribbon(line)

print(total_paper)
print(total_ribbon)
