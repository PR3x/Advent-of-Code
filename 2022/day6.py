command = ''

with open('2022/input_day6.txt', 'rt') as f:
    command = f.readline().strip()

for i in range(14, len(command)):
    ### PART 1
    # b = i - 4
    b = i - 14
    window = command[b:i]
    if len(window) == len(set(window)):
        print(i)
        print(window)
        exit(0)