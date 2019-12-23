"""
--- Day 12: The N-Body Problem ---
"""

import unittest
from typing import List


class Point:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __repr__(self):
        return f"<x={self.x}, y={self.y}, z={self.z}>"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def energy(self) -> int:
        return abs(self.x) + abs(self.y) + abs(self.z)


class Moon:
    def __init__(self, x, y, z, name=""):
        self.position = Point(x, y, z)
        self.velocity = Point(0, 0, 0)
        self.name = name

    def __repr__(self):
        return f"pos={self.position}, vel={self.velocity}, name={self.name}"

    def energy(self):
        potential = self.position.energy()
        kinetic = self.velocity.energy()
        return potential * kinetic


class System:
    def __init__(self, moons: List[Moon]):
        self.__moons = moons

    def step(self):
        self.__gravity()
        self.__velocity()

    def totalEnergy(self) -> int:
        return sum(moon.energy() for moon in self.__moons)

    def __gravity(self):
        for moon in self.__moons:
            for other in self.__moons:
                if other is moon:
                    # This is the same moon, do nothing
                    continue
                # x pos
                if moon.position.x < other.position.x:
                    moon.velocity.x += 1
                elif moon.position.x > other.position.x:
                    moon.velocity.x -= 1
                if moon.position.y < other.position.y:
                    moon.velocity.y += 1
                elif moon.position.y > other.position.y:
                    moon.velocity.y -= 1
                if moon.position.z < other.position.z:
                    moon.velocity.z += 1
                elif moon.position.z > other.position.z:
                    moon.velocity.z -= 1

    def __velocity(self):
        for moon in self.__moons:
            moon.position += moon.velocity

    def __repr__(self):
        return "\n".join(str(moon) for moon in self.__moons)


def input_parse(in_str: str) -> List:
    out = []
    for line in in_str.splitlines():
        line = line.strip("<")
        line = line.rstrip(">")
        line = line.split(",")
        x = int(line[0].split("=")[1])
        y = int(line[1].split("=")[1])
        z = int(line[2].split("=")[1])
        out.append(Moon(x, y, z))
    return out


class Part1(unittest.TestCase):
    def test1(self):
        io = Moon(-1, 0, 2, "Io")
        europa = Moon(2, -10, -7, "Europa")
        ganymede = Moon(4, -8, 8, "Ganymede")
        callisto = Moon(3, 5, -1, "Callisto")
        jupiter = System([io, europa, ganymede, callisto])
        jupiter.step()
        self.assertEqual(io.position, Moon(2, -1, 1).position)
        self.assertEqual(europa.position, Moon(3, -7, -4).position)
        self.assertEqual(ganymede.position, Moon(1, -7, 5).position)
        self.assertEqual(callisto.position, Moon(2, 2, 0).position)
        jupiter.step()
        self.assertEqual(io.position, Moon(5, -3, -1).position)
        self.assertEqual(europa.position, Moon(1, -2, 2).position)
        self.assertEqual(ganymede.position, Moon(1, -4, -1).position)
        self.assertEqual(callisto.position, Moon(1, -4, 2).position)
        jupiter.step()
        jupiter.step()
        jupiter.step()
        jupiter.step()
        jupiter.step()
        jupiter.step()
        jupiter.step()
        jupiter.step()
        # Step 10
        self.assertEqual(io.position, Moon(2, 1, -3).position)
        self.assertEqual(europa.position, Moon(1, -8, 0).position)
        self.assertEqual(ganymede.position, Moon(3, -6, 1).position)
        self.assertEqual(callisto.position, Moon(2, 0, 4).position)
        energy = jupiter.totalEnergy()
        self.assertEqual(energy, 179)

    def test2(self):
        in_str = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>
"""
        parsed = input_parse(in_str)
        jupiter = System(parsed)
        jupiter.step()
        jupiter.step()
        jupiter.step()
        jupiter.step()
        jupiter.step()
        jupiter.step()
        jupiter.step()
        jupiter.step()
        jupiter.step()
        jupiter.step()
        self.assertEqual(jupiter.totalEnergy(), 179)


def main():
    with open("2019/input_day12.txt", "r") as f:
        in_str = f.read()
    jupiter = System(input_parse(in_str))
    for _ in range(1000):
        jupiter.step()
    print(jupiter.totalEnergy())


if __name__ == "__main__":
    main()
