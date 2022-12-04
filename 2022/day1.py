elves = []

with open("./2022/input_day1.txt", "r") as f:
    elf = 0
    for line in f:
        line = line.strip()
        if line:
            elf += int(line)
        else:
            elves.append(elf)
            elf = 0  # new elf

# print(max(elves))
elf1 = max(elves)
elves.remove(elf1)
elf2 = max(elves)
elves.remove(elf2)
elf3 = max(elves)
print(elf1 + elf2 + elf3)
