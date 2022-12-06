def main():
    location = [0, 0, 0]
    with open('day2.txt', 'r') as f:
        for instruction in f:
            command, distance = instruction.split()
            distance = int(distance)
            if command == 'forward':
                location[0] += distance
                location[1] += distance * location[2]
            elif command == 'down':
                location[2] += distance
            elif command == 'up':
                location[2] -= distance
    print(location, location[0] * location[1])

if __name__ == "__main__":
    main()
