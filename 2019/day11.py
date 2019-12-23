"""
--- Day 11: Space Police ---
"""
import unittest

from typing import List
import threading  # Run isolated, stateful intcode computers
from queue import SimpleQueue  # Communication
from typing import NamedTuple
from enum import Enum, IntEnum

from intcode_computer import run
import sys


class Point(NamedTuple):
    x: int
    y: int

    def __add__(self, other):
        if isinstance(other, Direction):
            other = other.value
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self) -> str:
        return f"<Point ({self.x}, {self.y})>"


class Direction(Enum):
    UP = Point(0, 1)
    RIGHT = Point(1, 0)
    DOWN = Point(0, -1)
    LEFT = Point(-1, 0)

    def turn(self, direction):
        if direction == Direction.LEFT:
            if self.name == "UP":
                return Direction.LEFT
            elif self.name == "RIGHT":
                return Direction.UP
            elif self.name == "DOWN":
                return Direction.RIGHT
            elif self.name == "LEFT":
                return Direction.DOWN

        elif direction == Direction.RIGHT:
            if self.name == "UP":
                return Direction.RIGHT
            elif self.name == "RIGHT":
                return Direction.DOWN
            elif self.name == "DOWN":
                return Direction.LEFT
            elif self.name == "LEFT":
                return Direction.UP

    def __str__(self):
        if self.name == "UP":
            return "^"
        elif self.name == "RIGHT":
            return ">"
        elif self.name == "DOWN":
            return "v"
        elif self.name == "LEFT":
            return "<"


class PaintColor(IntEnum):
    WHITE = 1
    BLACK = 0

    def __str__(self):
        if self.name == "WHITE":
            return "#"
        elif self.name == "BLACK":
            return "-"


class PaintingRobot:
    def __init__(self, rom):
        self.facing = Direction.UP
        # communication channels
        self.input = SimpleQueue()
        self.output = SimpleQueue()
        self.painted = {}
        self.location = Point(0, 0)

        self.computer = threading.Thread(
            target=run, args=(rom, self.input, self.output)
        )

    def paint(self, color):
        if color == 0:
            self.painted[self.location] = PaintColor.BLACK
        elif color == 1:
            self.painted[self.location] = PaintColor.WHITE

    def turnAndMove(self, direction):
        if direction == 0:
            # turn left
            self.facing = self.facing.turn(Direction.LEFT)
        elif direction == 1:
            # turn right
            self.facing = self.facing.turn(Direction.RIGHT)
        self.location += self.facing

    def panelColor(self):
        if self.location in self.painted:
            return self.painted[self.location]
        else:
            return PaintColor.BLACK

    def run(self):
        self.computer.start()
        while self.computer.is_alive():
            self.input.put(self.panelColor())
            self.paint(self.output.get(timeout=5))
            self.turnAndMove(self.output.get(timeout=5))
            print(self)
            print(self.location)
            print("---------------")
        self.computer.join()

    def __str__(self) -> str:
        points = list(self.painted.keys())
        pointsx = [point.x for point in points] + [self.location.x]
        pointsy = [point.y for point in points] + [self.location.y]
        out = []
        for y in reversed(range(min(pointsy) - 1, max(pointsy) + 2)):
            tmp = []
            for x in range(min(pointsx) - 1, max(pointsx) + 2):
                loc = Point(x, y)
                if loc == self.location:
                    tmp.append(str(self.facing))
                elif loc in points:
                    tmp.append(str(self.painted[loc]))
                else:
                    tmp.append(".")
            out.append("".join(tmp))
        return "\n".join(out)


class TestWithoutIntcode(unittest.TestCase):
    def test1(self):
        robot = PaintingRobot("")
        self.assertEqual(robot.location, Point(0, 0))
        self.assertEqual(robot.panelColor(), 0)
        robot.paint(1)
        robot.turnAndMove(0)
        self.assertEqual(robot.facing, Direction.LEFT)
        self.assertEqual(robot.painted[Point(0, 0)], PaintColor.WHITE)
        self.assertEqual(robot.location, Point(-1, 0))
        self.assertEqual(robot.panelColor(), 0)
        robot.paint(0)
        robot.turnAndMove(0)
        robot.paint(1),
        robot.turnAndMove(0)
        robot.paint(1)
        robot.turnAndMove(0)
        print(robot)
        print("-----")
        self.assertEqual(robot.facing, Direction.UP)
        self.assertEqual(robot.location, Point(0, 0))
        self.assertEqual(robot.panelColor(), 1)
        robot.paint(0)
        robot.turnAndMove(1)
        robot.paint(1)
        robot.turnAndMove(0)
        robot.paint(1)
        robot.turnAndMove(0)
        print(robot)
        print("-----")
        self.assertEqual(robot.location, Point(0, 1))
        self.assertEqual(robot.facing, Direction.LEFT)
        self.assertEqual(len(robot.painted), 6)


def main():
    with open("2019/input_day11.txt", "r") as f:
        data = f.read()
    rom = [int(x) for x in data.split(",")] + [0] * 10000

    robot = PaintingRobot(rom)
    stdout = sys.stdout
    sys.stdout = open("2019/day11test.txt", "w")
    robot.run()
    sys.stdout = stdout
    print(robot.painted)
    print(len(robot.painted))


if __name__ == "__main__":
    main()
