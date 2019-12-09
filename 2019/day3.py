"""
--- Day 3: Crossed Wires ---
"""

import unittest
from typing import List, Dict, Tuple, Callable, Any

# Custom types
Wire = List[str]
Point = Tuple[int, int]
Grid = Dict[Point, int]


def draw_wire(grid: Grid, wire: Wire, marking: Any = 1) -> Grid:
    x = y = 0
    for path in wire:
        direction = path[0]
        distance = path[1:]

        for _ in range(int(distance)):
            if direction == "R":
                x += 1
            elif direction == "L":
                x -= 1
            elif direction == "U":
                y += 1
            elif direction == "D":
                y -= 1
            else:
                raise Exception("Unknown direction", direction)
            grid[(x, y)] = marking

    return grid


def find_intersections(grid: Grid, wire: Wire) -> List[Point]:
    # I know, duplicated code is bad, yada yada
    intersections = []
    x = y = 0

    for path in wire:
        direction = path[0]
        distance = path[1:]

        for _ in range(int(distance)):
            if direction == "R":
                x += 1
            elif direction == "L":
                x -= 1
            elif direction == "U":
                y += 1
            elif direction == "D":
                y -= 1
            else:
                raise Exception("Unknown direction", direction)

            if (x, y) in grid:
                # We have an intersection!
                intersections.append((x, y))

    return intersections


def trace_wire(grid: Grid, wire: Wire, intersections: List[Point]) -> Dict[Point, int]:
    # I know, duplicated code is bad, yada yada
    x = y = 0
    distances = {}
    length = 0

    for path in wire:
        direction = path[0]
        distance = path[1:]

        for _ in range(int(distance)):
            if direction == "R":
                x += 1
            elif direction == "L":
                x -= 1
            elif direction == "U":
                y += 1
            elif direction == "D":
                y -= 1
            else:
                raise Exception("Unknown direction", direction)
            length += 1

            if (x, y) in intersections:
                distances[(x, y)] = length

    return distances


def min_distance(wire1: Wire, wire2: Wire) -> int:
    grid = {}
    grid[(0, 0)] = "S"

    grid = draw_wire(grid, wire1)
    intersections = find_intersections(grid, wire2)

    return min(abs(x + y) for x, y in intersections)


def min_steps(wire1: Wire, wire2: Wire) -> int:
    grid = {}
    grid[(0, 0)] = "S"

    grid = draw_wire(grid, wire1)
    intersections = find_intersections(grid, wire2)

    distances1 = trace_wire(grid, wire1, intersections)
    distances2 = trace_wire(grid, wire2, intersections)

    combined_distances = []
    for point in distances1:
        combined_distances.append(distances1[point] + distances2[point])
    return min(combined_distances)


class Tester(unittest.TestCase):
    def test1(self):
        in1 = ["R8", "U5", "L5", "D3"]
        in2 = ["U7", "R6", "D4", "L4"]
        output = 6

        distance = min_distance(in1, in2)
        self.assertEqual(output, distance)

    def test2(self):
        # Don't know why this one fails, but it do
        # fmt: off
        in1 = ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"]
        in2 = ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]
        output = 159
        # fmt: on

        distance = min_distance(in1, in2)
        self.assertEqual(output, distance)

    def test3(self):
        # fmt: off
        in1 = ["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"]
        in2 = ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"]
        output = 135
        # fmt: on

        distance = min_distance(in1, in2)
        self.assertEqual(output, distance)


def main():
    wire1 = []
    wire2 = []
    with open("2019/input_day3.txt", "r") as f:
        wire1 = f.readline()[:-1].split(",")  # drop newline with [:-1]
        wire2 = f.readline()[:-1].split(",")
    print("Min Manhattan distance:", min_distance(wire1, wire2))
    print("Min steps:", min_steps(wire1, wire2))


if __name__ == "__main__":
    # unittest.main()
    main()
