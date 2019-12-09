"""
--- Day 2: 1202 Program Alarm ---
"""

import unittest


def run(rom):
    ram = rom.copy()  # Really need the copy for part 2. Otherwise, rom gets clobbered
    pc = 0
    opcode = ram[pc]
    while opcode != 99:
        input1 = ram[pc + 1]
        input2 = ram[pc + 2]
        output = ram[pc + 3]

        if opcode == 1:
            ram[output] = ram[input1] + ram[input2]
        elif opcode == 2:
            ram[output] = ram[input1] * ram[input2]
        else:
            raise Exception("Non-existant opcode", opcode, "Position:", pc)

        pc += 4
        opcode = ram[pc]

    return ram


class Test_Part1(unittest.TestCase):
    def test1(self):
        ram = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        result = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        self.assertEqual(run(ram), result)

    def test2(self):
        ram = [1, 0, 0, 0, 99]
        result = [2, 0, 0, 0, 99]
        self.assertEqual(run(ram), result)

    def test3(self):
        ram = [2, 4, 4, 5, 99, 0]
        result = [2, 4, 4, 5, 99, 9801]
        self.assertEqual(run(ram), result)

    def test4(self):
        ram = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        result = [30, 1, 1, 4, 2, 5, 6, 0, 99]
        self.assertEqual(run(ram), result)


if __name__ == "__main__":
    data = ""

    with open("2019/input_day2.txt", "r") as f:
        data = f.read()

    rom = list(map(int, data.split(",")))

    output = run(rom)
    print(output[0])

    for noun in range(99):
        for verb in range(99):
            testrom = rom
            testrom[1] = noun
            testrom[2] = verb
            output = run(rom)
            if output[0] == 19690720:
                print(noun, verb)
                break
