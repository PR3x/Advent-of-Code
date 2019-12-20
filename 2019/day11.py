"""
--- Day 11: Space Police ---
"""
import unittest

from typing import List
import threading  # Run isolated, stateful intcode computers
from queue import SimpleQueue  # Communication

from intcode_computer import run

class PaintingRobot:
    def __init__(self):
        self.facing = (0, 1)
        # communication channels
        self.input = SimpleQueue()
        self.output = SimpleQueue()
        self.painted = {}
        self.location = [0, 0]
    
    def turn(self, direction):
        pass

    def paint(self, color):
        pass

def main():
    with open("2019/input_day11.txt", "r") as f:
        data = f.read()
    rom = [int(x) for x in data.split(",")] + [0] * 10000
    # communication channels
    queue_in = SimpleQueue()
    queue_out = SimpleQueue()


if __name__ == "__main__":
    main()
