with open("2015\input_day1.txt", "rt") as f:
    input = f.readline().rstrip("\r\n")

### PART 1
# count = 0
# for char in input:
#     count = count + 1 if char == "(" else count - 1

# print(count)

### PART 2
floor = 0
for i in range(len(input)):  # need the position
    floor = floor + 1 if input[i] == "(" else floor - 1
    if floor < 0:
        print(i + 1)
        exit(0)
