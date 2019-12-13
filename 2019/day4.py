"""
--- Day 4: Secure Container ---
"""

import unittest


puzzle_input = "265275-781584"


def adjacent_digits(check: str) -> bool:
    prev = ""  # Extra few bytes of memory, but so what
    for char in check:
        if char == prev:
            return True
        prev = char
    return False


def increasing(check: str) -> bool:
    # Yikes, I don't like this algorithm. But it does work.
    for i in range(len(check)):
        for j in range(i):
            if int(check[i]) < int(check[j]):
                return False
    return True


def single_pair(check: str) -> bool:
    count = {}
    for i in range(len(check)):
        count[check[i]] = 1
        for j in range(i):
            if check[i] == check[j]:
                count[check[i]] += 1

    if 2 in count.values():
        return True
    return False


class Test_Part1(unittest.TestCase):
    def test1(self):
        ins = "111111"
        self.assertTrue(adjacent_digits(ins))
        self.assertTrue(increasing(ins))

    def test2(self):
        ins = "223450"
        self.assertTrue(adjacent_digits(ins))
        self.assertFalse(increasing(ins))

    def test3(self):
        ins = "123789"
        self.assertFalse(adjacent_digits(ins))
        self.assertTrue(increasing(ins))


class Test_Part2(unittest.TestCase):
    def test1(self):
        ins = "112233"
        self.assertTrue(single_pair(ins))
        self.assertTrue(increasing(ins))

    def test2(self):
        ins = "123444"
        self.assertFalse(single_pair(ins))
        self.assertTrue(increasing(ins))

    def test3(self):
        ins = "111122"
        self.assertTrue(single_pair(ins))
        self.assertTrue(increasing(ins))


def part1():
    count = 0
    for i in range(265275, 781584):
        inp = str(i)
        if adjacent_digits(inp) and increasing(inp):
            count += 1
    return count


def part2():
    count = 0
    for i in range(265275, 781584):
        inp = str(i)
        if single_pair(inp) and increasing(inp):
            count += 1
    return count


if __name__ == "__main__":
    unittest.main()
    # print(part1())
    # print(part2())
