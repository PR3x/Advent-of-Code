"""
--- Day 9: Sensor Boost ---
"""

from typing import List
import threading  # amps are separate computers
from queue import SimpleQueue  # Communication between amps

from itertools import permutations  # for all amp settings


def load(ram: List[int], pointer: int, mode: int, rb=0) -> int:
    if mode == 0:
        return int(ram[ram[pointer]])
    elif mode == 1:
        return int(ram[pointer])
    elif mode == 2:
        return int(ram[ram[pointer + rb]])


def run(rom: List[int], inq: SimpleQueue, out: SimpleQueue):
    output = None  # We're not printing it anymore. Move it up scope.
    ram = rom.copy()  # Otherwise, rom gets clobbered
    ip = 0  # instruction pointer
    rb = 0  # relative base
    while True:
        # Decode instruction
        instruction = str(ram[ip]).rjust(5, "0")
        # mode_parm3 = int(instruction[0])  # Currently unused
        mode_parm2 = int(instruction[1])
        mode_parm1 = int(instruction[2])
        opcode = int(instruction[3:5])

        # Execute
        # 99: Exit
        if opcode == 99:
            return output
        # 1: Add
        elif opcode == 1:
            ram[ram[ip + 3]] = load(ram, ip + 1, mode_parm1, rb) + load(
                ram, ip + 2, mode_parm2, rb
            )  # Writes will *never* be direct
            ip += 4
        # 2: Multiply
        elif opcode == 2:
            ram[ram[ip + 3]] = load(ram, ip + 1, mode_parm1, rb) * load(
                ram, ip + 2, mode_parm2, rb
            )
            ip += 4
        # 3: Input
        elif opcode == 3:
            ram[ram[ip + 1]] = inq.get()
            ip += 2
        # 4: Print
        elif opcode == 4:
            output = load(ram, ip + 1, mode_parm1, rb)
            # output = ram[ram[ip + 1]] if mode_parm1 == 0 else ram[ip + 1]
            # out.put(output)
            print(output)
            ip += 2
        # 5: Jump if True
        elif opcode == 5:
            if load(ram, ip + 1, mode_parm1, rb) != 0:
                ip = load(ram, ip + 2, mode_parm2, rb)
            else:
                ip += 3
        # 6: Jump if False
        elif opcode == 6:
            if load(ram, ip + 1, mode_parm1, rb) == 0:
                ip = load(ram, ip + 2, mode_parm2, rb)
            else:
                ip += 3
        # 7: Less than
        elif opcode == 7:
            if load(ram, ip + 1, mode_parm1, rb) < load(ram, ip + 2, mode_parm2, rb):
                ram[ram[ip + 3]] = 1
            else:
                ram[ram[ip + 3]] = 0
            ip += 4
        # 8: Equals
        elif opcode == 8:
            if load(ram, ip + 1, mode_parm1, rb) == load(ram, ip + 2, mode_parm2, rb):
                ram[ram[ip + 3]] = 1
            else:
                ram[ram[ip + 3]] = 0
            ip += 4
        elif opcode == 9:
            rb += load(ram, ip + 1, mode_parm1, rb)
            ip += 2
        else:
            raise Exception("Unknown opcode", opcode)


def main():
    data = ""
    with open("2019/input_day9.txt", "r") as f:
        data = f.read()

    # test data
    data = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"

    rom = [int(x) for x in data.split(",")] + [0] * 10000

    # communication channels
    queue_in = SimpleQueue()
    # queue_in.put()
    queue_out = SimpleQueue()
    # queue_out.put()

    # computer
    run(rom, queue_in, queue_out)
    # boost = threading.Thread(target=run, args=(rom, queue_out, queue_in))
    # boost.start()
    # boost.join()
    # print(queue_out.get(False))


if __name__ == "__main__":
    main()
