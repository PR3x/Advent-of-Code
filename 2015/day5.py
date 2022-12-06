def part1(line: str) -> bool:
    if any(naughty in line for naughty in ['ab', 'cd', 'pq', 'xy']):
        return False
    vowel_count = 0
    double_letter = False
    prev_char = ''
    for char in line:
        if char == 'a' or char=='e' or char=='i' or char=='o' or char=='u':
            vowel_count += 1
        if char == prev_char:
            double_letter = True
        prev_char = char
    return vowel_count >= 3 and double_letter

def part2(line) -> bool:
    repeat_pair = False
    repeat_after_one = False

    line_len = len(line)
    for i in range(line_len):
        if i != 0 and not repeat_pair:
            pair = f"{line[i-1]}{line[i]}"
            if pair in line[i+1:]:
                repeat_pair = True
        try:
            if line[i] == line[i+2]:
                repeat_after_one = True
        except IndexError:
            pass  

    return repeat_pair and repeat_after_one

out = 0

with open('2015/input_day5.txt', 'rt') as f:
    for line in f:
        line = line.rstrip()
        # if part1(line):
        if part2(line):
            out += 1

print(out)
