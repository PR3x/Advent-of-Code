with open("2015\input_day3.txt", "rt") as f:
    input = f.readline().rstrip("\r\n")

### PART 1
# x = 0
# y = 0
# houses = [(x, y)]  # deliver to starting position

# for direction in input:
#     if direction == "<":
#         y -= 1
#     elif direction == ">":
#         y += 1
#     elif direction == "^":
#         x += 1
#     elif direction == "v":
#         x -= 1
#     houses.append((x, y))
#
# print(len(set(houses)))

### PART 2
s_x = 0
s_y = 0
r_x = 0
r_y = 0
houses = [(s_x, s_y), (r_x, r_y)]  # deliver to starting position

for i in range(0, len(input)-1, 2):
    s_direction = input[i]
    r_direction = input[i+1]
    if s_direction == "<":
        s_y -= 1
    elif s_direction == ">":
        s_y += 1
    elif s_direction == "^":
        s_x += 1
    elif s_direction == "v":
        s_x -= 1
    houses.append((s_x,s_y))

    if r_direction == "<":
        r_y -= 1
    elif r_direction == ">":
        r_y += 1
    elif r_direction == "^":
        r_x += 1
    elif r_direction == "v":
        r_x -= 1
    houses.append((r_x,r_y))

print(len(set(houses)))