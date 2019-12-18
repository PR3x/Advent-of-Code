"""
--- Day 10: Monitoring Station ---
"""

import unittest
from typing import Tuple, List, Dict
import math
from copy import copy

Coordinate = Tuple[int, int]


class AsteroidMap:
    def __init__(self, data: str = None):
        if data:
            self.__processData(data)

    def __processData(self, data: str):
        self.__asteroids = {}
        split = data.split()
        self.__xdim = len(split[0])  # Assuming rectangular map
        self.__ydim = len(split)  # These *may* be used later for __str__()
        y = 0
        for line in split:
            x = 0
            for elem in line:
                if self.__isAsteroid(elem):
                    self.__asteroids[(x, y)] = 0
                x += 1
            y += 1

    def sweepAsteroids(self):
        for asteroid in self.__asteroids:
            self.__asteroids[asteroid] = len(self.__radarSweep(asteroid))
        pass

    def __radarSweep(self, asteroid: Coordinate) -> List[Coordinate]:
        seen_asteroids = {}
        count = 0
        for a in self.__asteroids:
            if a == asteroid:  # This is ourselves
                continue
            angle = math.atan2(a[1] - asteroid[1], a[0] - asteroid[0])
            angle = angle
            if not angle in seen_asteroids:
                seen_asteroids[angle] = a
        sorted_angles = dict(
            sorted(
                seen_asteroids.items(),
                key=lambda coord: ((coord[0] + (3 * math.pi / 2)) % (2 * math.pi)),
                reverse=True,
            )
        )
        # sorted_angles.insert(0, sorted_angles.pop())  # start, not end, straight up

        out = list(sorted_angles.values())
        out.insert(0, out.pop())
        return out

    @staticmethod
    def __specAngleSort(coord: Coordinate):
        return (coord[0] + (3 * math.pi / 2)) % (2 * math.pi)

    @staticmethod
    def __isAsteroid(char: str) -> bool:
        return char == "#"  # `#` is defined as the asteroid character in problem

    def monitorLocation(self) -> Tuple[Coordinate, int]:
        inv_map = {v: k for k, v in self.__asteroids.items()}  # Invert map - num:coord
        max_found = max(inv_map.keys())  # largest key/number found
        return (inv_map[max_found], max_found)

    def pewpew(self, asteroid: Coordinate) -> List[Coordinate]:
        start_angle = math.pi / 2
        pew_map = copy(self)  # deleting asteroids on the copy of ourselves
        out = []
        while len(pew_map.__asteroids) != 1:  # The one asteroid we're sitting on
            pewed = pew_map.__radarSweep(asteroid)
            out += pewed
            pew_map.__asteroids = [
                asteroid for asteroid in pew_map.__asteroids if asteroid not in pewed
            ]
        return out


class MapTester(unittest.TestCase):
    def test1(self):
        mapdata = """.#..#
.....
#####
....#
...##"""
        amap = AsteroidMap(mapdata)
        amap.sweepAsteroids()
        output, count = amap.monitorLocation()
        self.assertEqual(output, (3, 4))
        self.assertEqual(count, 8)

    def test2(self):
        mapdata = """......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####"""
        amap = AsteroidMap(mapdata)
        amap.sweepAsteroids()
        output, count = amap.monitorLocation()
        self.assertEqual(output, (5, 8))
        self.assertEqual(count, 33)

    def test3(self):
        mapdata = """#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##.
..##....##
......#...
.####.###."""
        amap = AsteroidMap(mapdata)
        amap.sweepAsteroids()
        output, count = amap.monitorLocation()
        self.assertEqual(output, (1, 2))
        self.assertEqual(count, 35)

    def test4(self):
        mapdata = """.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#.."""
        amap = AsteroidMap(mapdata)
        amap.sweepAsteroids()
        output, count = amap.monitorLocation()
        self.assertEqual(output, (6, 3))
        self.assertEqual(count, 41)

    def test5(self):
        mapdata = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##"""
        amap = AsteroidMap(mapdata)
        amap.sweepAsteroids()
        output, count = amap.monitorLocation()
        self.assertEqual(output, (11, 13))
        self.assertEqual(count, 210)


class PewTester(unittest.TestCase):
    def test1(self):
        mapdata = """.#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....#...###..
..#.#.....#....##"""
        # station should be at (8,3)
        amap = AsteroidMap(mapdata)
        amap.sweepAsteroids()
        output, count = amap.monitorLocation()
        self.assertEqual(output, (8, 3))
        pewlist = amap.pewpew((8, 3))

    def test2(self):
        mapdata = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##"""
        amap = AsteroidMap(mapdata)
        amap.sweepAsteroids()
        output, count = amap.monitorLocation()
        self.assertEqual(output, (11, 13))
        self.assertEqual(count, 210)
        pewlist = amap.pewpew(output)
        self.assertEqual(pewlist[0], (11, 12))
        self.assertEqual(pewlist[1], (12, 1))
        self.assertEqual(pewlist[2], (12, 2))
        self.assertEqual(pewlist[9], (12, 8))
        self.assertEqual(pewlist[19], (16, 0))
        self.assertEqual(pewlist[49], (16, 9))
        self.assertEqual(pewlist[99], (10, 16))
        self.assertEqual(pewlist[199], (8, 2))
        self.assertEqual(pewlist[200], (10, 9))
        self.assertEqual(pewlist[298], (11, 1))


def main():
    with open("2019/input_day10.txt", "r") as f:
        data_in = f.read()
    amap = AsteroidMap(data_in)
    amap.sweepAsteroids()
    output, count = amap.monitorLocation()
    print("Detected", count, "asteroids")


if __name__ == "__main__":
    unittest.main()
    # main()
