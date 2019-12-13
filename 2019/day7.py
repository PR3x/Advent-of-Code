"""
--- Day 7: Amplification Circuit ---
"""

from typing import List
import threading  # amps are separate computers
from queue import SimpleQueue  # Communication between amps

from itertools import permutations  # for all amp settings


def load(ram: List[int], pointer: int, mode: int) -> int:
    if mode == 0:
        return int(ram[ram[pointer]])
    elif mode == 1:
        return int(ram[pointer])


def run(rom: List[int], inp: SimpleQueue, out: SimpleQueue):
    output = None  # We're not printing it anymore. Move it up scope.
    ram = rom.copy()  # Otherwise, rom gets clobbered
    ip = 0
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
            ram[ram[ip + 3]] = load(ram, ip + 1, mode_parm1) + load(
                ram, ip + 2, mode_parm2
            )  # Writes will *never* be direct
            ip += 4
        # 2: Multiply
        elif opcode == 2:
            ram[ram[ip + 3]] = load(ram, ip + 1, mode_parm1) * load(
                ram, ip + 2, mode_parm2
            )
            ip += 4
        # 3: Input
        elif opcode == 3:
            ram[ram[ip + 1]] = inp.get()
            ip += 2
        # 4: Print
        elif opcode == 4:
            output = ram[ram[ip + 1]] if mode_parm1 == 0 else ram[ip + 1]
            out.put(output)
            # print(output)
            ip += 2
        # 5: Jump if True
        elif opcode == 5:
            if load(ram, ip + 1, mode_parm1) != 0:
                ip = load(ram, ip + 2, mode_parm2)
            else:
                ip += 3
        # 6: Jump if False
        elif opcode == 6:
            if load(ram, ip + 1, mode_parm1) == 0:
                ip = load(ram, ip + 2, mode_parm2)
            else:
                ip += 3
        # 7: Less than
        elif opcode == 7:
            if load(ram, ip + 1, mode_parm1) < load(ram, ip + 2, mode_parm2):
                ram[ram[ip + 3]] = 1
            else:
                ram[ram[ip + 3]] = 0
            ip += 4
        # 8: Equals
        elif opcode == 8:
            if load(ram, ip + 1, mode_parm1) == load(ram, ip + 2, mode_parm2):
                ram[ram[ip + 3]] = 1
            else:
                ram[ram[ip + 3]] = 0
            ip += 4
        else:
            raise Exception("Unknown opcode", opcode)


def main():
    data = ""
    with open("2019/input_day7.txt", "r") as f:
        data = f.read()

    rom = [int(x) for x in data.split(",")]
    out = {}
    for p in permutations(range(5, 10)):
        pstr = "".join(str(e) for e in p)

        # communication channels
        qab = SimpleQueue()
        qab.put(p[1])
        qbc = SimpleQueue()
        qbc.put(p[2])
        qcd = SimpleQueue()
        qcd.put(p[3])
        qde = SimpleQueue()
        qde.put(p[4])
        qea = SimpleQueue()
        qea.put(p[0])

        # amplifier computers
        ampa = threading.Thread(target=run, args=(rom, qea, qab))
        ampb = threading.Thread(target=run, args=(rom, qab, qbc))
        ampc = threading.Thread(target=run, args=(rom, qbc, qcd))
        ampd = threading.Thread(target=run, args=(rom, qcd, qde))
        ampe = threading.Thread(target=run, args=(rom, qde, qea))

        ampa.start()
        ampb.start()
        ampc.start()
        ampd.start()
        ampe.start()

        qea.put(0)  # start the chain

        ampa.join()
        ampb.join()
        ampc.join()
        ampd.join()
        ampe.join()

        out[qea.get()] = pstr
    max_signal = max(out.keys())
    print("Max signal:", max_signal, "From", out[max_signal])


if __name__ == "__main__":
    main()
