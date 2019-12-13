"""
--- Day 1: The Tyranny of the Rocket Equation ---
"""

import math
import unittest


class SpacecraftModule:
    """Generic module with mass
    
    (Part 1)"""

    def __init__(self, mass: int):
        self.mass = mass

    def required_fuel(self, mass: int = False) -> int:
        if not mass:
            mass = self.mass
        return math.floor(mass / 3) - 2


class SpacecraftModule2(SpacecraftModule):
    """Module that has to carry its own fuel weight
    
    (Part 2)"""

    def __init__(self, mass: int):
        super().__init__(mass)

    def required_fuel(self) -> int:
        total = 0
        req_fuel = super().required_fuel(self.mass)
        while req_fuel > 0:
            total += req_fuel
            req_fuel = super().required_fuel(req_fuel)
        return total


class Spacecraft:
    """Collection of modules"""

    def __init__(self):
        self.modules = []

    def add_module(self, module: SpacecraftModule):
        self.modules.append(module)

    def total_fuel(self) -> int:
        return sum(mod.required_fuel() for mod in self.modules)


class TestSpacecraftModule(unittest.TestCase):
    def test_modules(self):
        mod1 = SpacecraftModule(12)
        mod2 = SpacecraftModule(14)
        mod3 = SpacecraftModule(1969)
        mod4 = SpacecraftModule(100756)
        modules = [mod1, mod2, mod3, mod4]

        self.assertEqual(mod1.required_fuel(), 2)
        self.assertEqual(mod2.required_fuel(), 2)
        self.assertEqual(mod3.required_fuel(), 654)
        self.assertEqual(mod4.required_fuel(), 33583)

        total = sum(mod.required_fuel() for mod in modules)
        self.assertEqual(total, 34241)


class TestSpacecraft(unittest.TestCase):
    def test_spacecraft(self):
        craft = Spacecraft()

        mod1 = SpacecraftModule2(14)
        mod2 = SpacecraftModule2(1969)
        mod3 = SpacecraftModule2(100756)

        craft.add_module(mod1)
        craft.add_module(mod2)
        craft.add_module(mod3)

        self.assertEqual(craft.total_fuel(), 51314)


if __name__ == "__main__":
    # unittest.main()
    craft = Spacecraft()
    with open('./2019/input_day1.txt', 'r') as inp:
        for item in inp:
            craft.add_module(SpacecraftModule2(int(item)))
    total = craft.total_fuel()
    print(total)
