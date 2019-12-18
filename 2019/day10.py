"""
--- Day 10: Monitoring Station ---
"""

import unittest
from typing import Tuple, Optional
from math import atan2

Coordinate = Tuple[int, int]


class AsteroidMap:
    def __init__(self, data: str = None):
        if data:
            self.__processData(data)

    def __processData(self, data: str):
        self.__asteroids = {}
        split = data.split()
        self.__xdim = len(split[0])  # Assuming rectangular map
        self.__ydim = len(split)
        y = 0
        for line in split:
            x = 0
            for elem in line:
                if self.__isAsteroid(elem):
                    self.__asteroids[(x, y)] = 0
                x += 1
            y += 1
        for asteroid in self.__asteroids:
            self.__asteroids[asteroid] = self.__radarSweep(asteroid)
        pass

    def __radarSweep(self, asteroid: Coordinate) -> int:
        seen = set()
        count = 0
        for a in self.__asteroids:
            if a == asteroid:  # This is ourselves
                # seen.add(None)
                continue
            angle = atan2(a[1] - asteroid[1], a[0] - asteroid[0])
            if not angle in seen:
                seen.add(angle)
        return len(seen)

    @staticmethod
    def __isAsteroid(char: str) -> bool:
        return char == "#"  # `#` is defined as the asteroid character in problem

    def monitorLocation(self) -> Tuple[Coordinate, int]:
        inv_map = {v: k for k, v in self.__asteroids.items()}
        max_found = max(inv_map.keys())
        return (inv_map[max_found], max_found)

    def __str__(self):
        return ""


class MapTester(unittest.TestCase):
    def test1(self):
        mapdata = """.#..#
.....
#####
....#
...##"""
        amap = AsteroidMap(mapdata)
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
        temp = str(amap)
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
        output, count = amap.monitorLocation()
        self.assertEqual(output, (11, 13))
        self.assertEqual(count, 210)


if __name__ == "__main__":
    unittest.main()
