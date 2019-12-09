"""
--- Day 5: Sunny with a Chance of Asteroids ---
"""

import unittest
from unittest.mock import patch


def run(rom):
    # Initially copied from Day 2
    ram = rom.copy()  # Otherwise, rom gets clobbered
    pc = 0
    while True:
        instruction = str(ram[pc]).rjust(5, "0")
        mode_parm3 = int(instruction[0])
        mode_parm2 = int(instruction[1])
        mode_parm3 = int(instruction[2])
        opcode = int(instruction[3:5])

        if opcode == 1:
            ram[ram[pc + 3]] = ram[ram[pc + 1]] + ram[ram[pc + 2]]
            pc += 4
        elif opcode == 2:
            ram[ram[pc + 3]] = ram[ram[pc + 1]] * ram[ram[pc + 2]]
            pc += 4
        elif opcode == 3:
            temp = input("> ")
            ram[ram[pc + 1]] = temp
        elif opcode == 4:
            print(ram[ram[pc + 1]])
            pc += 2
        elif opcode == 99:
            break
        else:
            raise Exception("Non-existant opcode", opcode, "Position:", pc)

    return ram


class TestRunner(unittest.TestCase):
    def test1(self):
        rom = "1101,100,-1,4,0".split(",")
        out = run(rom)
        self.assertEqual(out[4], 99)


if __name__ == "__main__":
    unittest.main()
