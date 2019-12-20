"""Intcode Computer
"""

from typing import List
from queue import SimpleQueue  # Communication


def _get_address(ram: List[int], pointer: int, mode: int, rb: int = 0) -> int:
    if mode == 0:
        return ram[pointer]
    if mode == 1:
        return pointer
    if mode == 2:
        return ram[pointer] + rb


def run(rom: List[int], inq: SimpleQueue, out: SimpleQueue):
    output = None  # We're not printing it anymore. Move it up scope.
    ram = rom.copy()  # Otherwise, rom gets clobbered
    ip = 0  # instruction pointer
    rb = 0  # relative base
    while True:
        # Decode instruction
        instruction = str(ram[ip]).rjust(5, "0")
        mode_parm3 = int(instruction[0])
        mode_parm2 = int(instruction[1])
        mode_parm1 = int(instruction[2])
        opcode = int(instruction[3:5])

        # Execute
        # 99: Exit
        if opcode == 99:
            return output
        # 1: Add
        elif opcode == 1:
            ram[_get_address(ram, ip + 3, mode_parm3, rb)] = (
                ram[_get_address(ram, ip + 1, mode_parm1, rb)]
                + ram[_get_address(ram, ip + 2, mode_parm2, rb)]
            )
            ip += 4
        # 2: Multiply
        elif opcode == 2:
            ram[_get_address(ram, ip + 3, mode_parm3, rb)] = (
                ram[_get_address(ram, ip + 1, mode_parm1, rb)]
                * ram[_get_address(ram, ip + 2, mode_parm2, rb)]
            )
            ip += 4
        # 3: Input
        elif opcode == 3:
            ram[_get_address(ram, ip + 3, mode_parm3, rb)] = inq.get()
            ip += 2
        # 4: Print
        elif opcode == 4:
            output = ram[_get_address(ram, ip + 1, mode_parm1, rb)]
            out.put(output)
            ip += 2
        # 5: Jump if True
        elif opcode == 5:
            if ram[_get_address(ram, ip + 1, mode_parm1, rb)] != 0:
                ip = ram[_get_address(ram, ip + 2, mode_parm2, rb)]
            else:
                ip += 3
        # 6: Jump if False
        elif opcode == 6:
            if ram[_get_address(ram, ip + 1, mode_parm1, rb)] == 0:
                ip = ram[_get_address(ram, ip + 2, mode_parm2, rb)]
            else:
                ip += 3
        # 7: Less than
        elif opcode == 7:
            if (
                ram[_get_address(ram, ip + 1, mode_parm1, rb)]
                < ram[_get_address(ram, ip + 2, mode_parm2, rb)]
            ):
                ram[_get_address(ram, ip + 3, mode_parm3, rb)] = 1
            else:
                ram[_get_address(ram, ip + 3, mode_parm3, rb)] = 0
            ip += 4
        # 8: Equals
        elif opcode == 8:
            if (
                ram[_get_address(ram, ip + 1, mode_parm1, rb)]
                == ram[_get_address(ram, ip + 2, mode_parm2, rb)]
            ):
                ram[_get_address(ram, ip + 3, mode_parm3, rb)] = 1
            else:
                ram[_get_address(ram, ip + 3, mode_parm3, rb)] = 0
            ip += 4
        # 9: Set relative
        elif opcode == 9:
            rb += ram[_get_address(ram, ip + 1, mode_parm1, rb)]
            ip += 2
        else:
            raise Exception("Unknown opcode", opcode)
