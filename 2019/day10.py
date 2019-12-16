"""
--- Day 10: Monitoring Station ---
"""

import unittest
from typing import Tuple

Coordinate = Tuple[int, int]


class AsteroidMap:
    def __init__(self, data):
        self.data = data

    def monitorLocation(self) -> Coordinate:
        return (0, 0)


class MapTester(unittest.TestCase):
    def test1(self):
        mapdata = ".#..#\n.....\n#####\n....#\n...##"
        amap = AsteroidMap(mapdata)
        output = amap.monitorLocation()
        self.assertEqual(output, (3, 4))

    def test2(self):
        mapdata = "......#.#.\n#..#.#....\n..#######.\n.#.#.###..\n.#..#.....\n..#....#.#\n#..#....#.\n.##.#..###\n##...#..#.\n.#....####"
        amap = AsteroidMap(mapdata)
        output = amap.monitorLocation()
        self.assertEqual(output, (5, 8))

    def test3(self):
        mapdata = "#.#...#.#.\n.###....#.\n.#....#...\n##.#.#.#.#\n....#.#.#.\n.##..###.#\n..#...##.\n..##....##\n......#...\n.####.###."
        amap = AsteroidMap(mapdata)
        output = amap.monitorLocation()
        self.assertEqual(output, (1, 2))

    def test4(self):
        mapdata = ".#..#..###\n####.###.#\n....###.#.\n..###.##.#\n##.##.#.#.\n....###..#\n..#.#..#.#\n#..#.#.###\n.##...##.#\n.....#.#.."
        amap = AsteroidMap(mapdata)
        output = amap.monitorLocation()
        self.assertEqual(output, (1, 2))

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
        output = amap.monitorLocation()
        self.assertEqual(output, (1, 2))


if __name__ == "__main__":
    unittest.main()
