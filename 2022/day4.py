count = 0

with open("2022/input_day4.txt", "r") as f:
    for line in f:
        line = line.strip()
        ranges = line.split(",")
        start1, end1 = map(int, ranges[0].split("-"))
        start2, end2 = map(int, ranges[1].split("-"))

        # part 1
        # if (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1):
        #     count += 1

        # part 2
        if (
            start1 == start2
            or start1 == end2
            or end1 == start2
            or end1 == end2
            or (start1 <= start2 and end1 >= start2)
            or (start2 <= start1 and end2 >= start1)
        ):
            count += 1

print(count)
