"""
--- Day 10: Monitoring Station ---
"""

import unittest
from typing import Tuple
from math import gcd

Coordinate = Tuple[int, int]


class AsteroidMap:
    def __init__(self, data: str):
        self.__elements = {}
        self.__processed = {}
        split = data.split()
        self.__xdim = len(split[0])  # Assuming rectangular map
        self.__ydim = len(split)
        self.strmap = ["."] * (self.__xdim * self.__ydim)
        # This seems to avoid bad copies
        # build map
        y = 0
        for line in split:
            x = 0
            for elem in line:
                self.__elements[(x, y)] = elem
                x += 1
            y += 1
        # go through again, process map
        y = 0
        for line in split:
            x = 0
            for elem in line:
                if not self.isAsteroid((x, y)):
                    x += 1
                    continue
                count = self.__radarSweep((x, y))
                if count != 0:
                    temp = x + (y * self.__ydim)  # TODO delete me
                    self.strmap[x + (y * self.__ydim)] = str(count)
                if not count in self.__processed:
                    self.__processed[count] = [(x, y)]
                else:
                    self.__processed[count].append((x, y))
                x += 1
            y += 1

    def __radarSweep(self, coordinate: Coordinate) -> int:
        xcor, ycor = coordinate
        visited = set()
        asteroid_count = 0
        for y in range(-self.__ydim + 1, self.__ydim):
            if y + ycor >= self.__ydim or y + ycor < 0:
                continue  # out of range
            for x in range(-self.__xdim + 1, self.__xdim):
                if x + xcor >= self.__xdim or x + xcor < 0:
                    continue  # also out of range
                ray = (0, 0)
                if x == 0:
                    # we need to avoid 0 division
                    if y == 0:
                        ray = (0, 0)
                    elif y < 0:
                        ray = (0, -1)
                    elif y > 0:
                        ray = (0, 1)
                else:
                    denom = gcd(y, x)
                    ray = (y // denom, x // denom)
                if ray in visited:
                    continue  # we've processed this slope, do nothing
                visited.add(ray)
                asteroid_count += self.__processSlope(coordinate, ray)
        return asteroid_count

    def __processSlope(self, coordinate: Coordinate, ray: Coordinate) -> int:
        if not self.isAsteroid(coordinate):
            return 0
        # Count self only if ray is (0, 0)
        if ray == (0, 0):
            return 1
        plusx, plusy = ray
        x, y = coordinate  # starting here, follow ray
        asteroid_count = 0
        x += plusx
        y += plusy
        while x >= 0 and y >= 0 and x < self.__xdim and y < self.__ydim:
            if self.isAsteroid((x, y)):
                asteroid_count += 1
                break
            x += plusx
            y += plusy
        return asteroid_count

    def isAsteroid(self, coordinate: Coordinate) -> bool:
        return self.__elements[coordinate] == "#"

    def monitorLocation(self) -> Tuple[Coordinate, int]:
        maxCount = max(self.__processed.keys())
        ret = (self.__processed[maxCount][0], maxCount)
        return ret

    def __str__(self):
        strmap = "".join(self.strmap)
        out = ""
        count = 0
        for s in strmap:
            out += s
            count += 1
            if count % self.__ydim == 0:
                out += "\n"
        return out


class MapTester(unittest.TestCase):
    def test1(self):
        mapdata = """.#..#
.....
#####
....#
...##"""
        amap = AsteroidMap(mapdata)
        temp = str(amap)
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
        self.assertEqual(output, (1, 2))
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
        self.assertEqual(output, (1, 2))
        self.assertEqual(count, 210)


if __name__ == "__main__":
    unittest.main()
