"""
--- Day 8: Space Image Format ---
"""

import unittest
from typing import List


class Layer:
    def __init__(self, data: List[str]):
        self.__data = data

    def __eq__(self, other):
        return self.__data == other.__data
    
    def count(self, value):
        return sum(x.count(value) for x in self.__data)


class Image:
    def __init__(self, data: str, width: int, height: int):
        self.__layers = []

        idx = 0
        while idx < len(data):
            layer = []
            for _ in range(height):
                layer.append(data[idx : idx + width])
                idx += width
            self.__layers.append(Layer(layer))
    
    def part1(self):
        zeroes = [layer.count("0") for layer in self.__layers]
        minlayer = self.__layers[zeroes.index(min(zeroes))]
        return minlayer.count("1") * minlayer.count("2")


def main():
    data = ""
    with open("2019/input_day8.txt", "r") as f:
        data = f.readline().strip()
    image = Image(data, 25, 6)
    print(image.part1())


class Test1(unittest.TestCase):
    def test1(self):
        data = "123456789012"
        image1 = Image(data, 3, 2)
        self.assertEqual(image1.__layers[0], Layer(["123", "456"]))
        self.assertEqual(image1.__layers[1], Layer(["789", "012"]))


if __name__ == "__main__":
    main()
    # unittest.main()
