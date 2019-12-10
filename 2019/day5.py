"""
--- Day 5: Sunny with a Chance of Asteroids ---
"""


def run(rom):
    # Initially copied from Day 2
    ram = rom.copy()  # Otherwise, rom gets clobbered
    ip = 0
    while True:
        instruction = str(ram[ip]).rjust(5, "0")
        mode_parm3 = int(instruction[0])
        mode_parm2 = int(instruction[1])
        mode_parm1 = int(instruction[2])
        opcode = int(instruction[3:5])
        instruction_length = 0

        # Load parameters into "registers"
        parm1 = 0
        if mode_parm1 == 0:  # indirect
            parm1 = int(ram[ram[ip + 1]])
        elif mode_parm1 == 1:  # direct
            parm1 = int(ram[ip + 1])

        parm2 = 0
        if mode_parm2 == 0:  # indirect
            parm2 = int(ram[ram[ip + 1]])
        elif mode_parm2 == 1:  # direct
            parm2 = int(ram[ip + 1])

        if opcode == 1:
            ram[ram[ip + 3]] = parm1 + parm2  # Writes will *never* be direct
            instruction_length = 4
        elif opcode == 2:
            ram[ram[ip + 3]] = parm1 * parm2
            instruction_length = 4
        elif opcode == 3:
            temp = int(input("> "))
            ram[ram[ip + 1]] = temp
            instruction_length = 2
        elif opcode == 4:
            output = ram[ram[ip + 1]] if mode_parm3 == 0 else ram[ip + 1]
            print(output)
            instruction_length = 2
        elif opcode == 99:
            break
        else:
            raise Exception("Non-existant opcode", opcode, "Position:", ip)

        ip += instruction_length

    return ram


def main():
    data = ""
    with open("2019/input_day5.txt", "r") as f:
        data = f.read()

    rom = [int(x) for x in data.split(",")]
    output = run(rom)

    print(output[0])


if __name__ == "__main__":
    main()
