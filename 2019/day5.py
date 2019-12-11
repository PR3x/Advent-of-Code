"""
--- Day 5: Sunny with a Chance of Asteroids ---
"""


def run(rom):
    # Initially copied from Day 2
    ram = rom.copy()  # Otherwise, rom gets clobbered
    ip = 0
    while True:
        instruction = str(ram[ip]).rjust(5, "0")
        mode_parm3 = int(instruction[0])  # currently unused
        mode_parm2 = int(instruction[1])
        mode_parm1 = int(instruction[2])
        opcode = int(instruction[3:5])

        # Run short instructions earliest so we don't try to read extra ram
        if opcode == 99:
            break
        elif opcode == 3:
            # temp = int(input("> "))  # Will always be 1 for this problem
            temp = 1
            ram[ram[ip + 1]] = temp
            ip += 2
            continue
        elif opcode == 4:
            output = ram[ram[ip + 1]] if mode_parm1 == 0 else ram[ip + 1]
            print(output)
            ip += 2
            continue

        # Load parameters into "registers"
        parm1 = 0
        if mode_parm1 == 0:  # indirect
            parm1 = int(ram[ram[ip + 1]])
        elif mode_parm1 == 1:  # direct
            parm1 = int(ram[ip + 1])

        parm2 = 0
        if mode_parm2 == 0:  # indirect
            parm2 = int(ram[ram[ip + 2]])
        elif mode_parm2 == 1:  # direct
            parm2 = int(ram[ip + 2])

        if opcode == 1:
            ram[ram[ip + 3]] = parm1 + parm2  # Writes will *never* be direct
            ip += 4
        elif opcode == 2:
            ram[ram[ip + 3]] = parm1 * parm2
            ip += 4

    return ram


def main():
    data = ""
    with open("2019/input_day5.txt", "r") as f:
        data = f.read()

    rom = [int(x) for x in data.split(",")]
    run(rom)


if __name__ == "__main__":
    main()
