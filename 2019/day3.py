"""
--- Day 3: Crossed Wires ---
"""

import unittest


class Tester(unittest.TestCase):
    def test1(self):
        in1 = ["R8", "U5", "L5", "D3"]
        in2 = ["U7", "R6", "D4", "L4"]
        output = 6

        distance = 0  # run program here
        self.assertEqual(output, distance)

    def test2(self):
        # fmt: off
        in1 = ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"]
        in2 = ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]
        output = 159
        # fmt: on

        distance = 0  # run program here
        self.assertEqual(output, distance)

    def test3(self):
        # fmt: off
        in1 = ["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"]
        in2 = ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"]
        output = 135
        # fmt: on

        distance = 0  # run program here
        self.assertEqual(output, distance)

if __name__ == "__main__":
    unittest.main()