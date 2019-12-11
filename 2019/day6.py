"""
--- Day 6: Universal Orbit Map ---
"""

import unittest
from typing import Dict, Set, Tuple


def orbit_map(orbit_str: str) -> Tuple[Dict[str, Set[str]]]:
    orbit_map = {}
    orbits = orbit_str.splitlines()
    for orbit in orbits:
        parent, child = orbit.split(")")
        if not parent in orbit_map:
            orbit_map[parent] = set([])
        if not child in orbit_map:
            orbit_map[child] = set([])
        orbit_map[parent].add(child)

    return orbit_map


def orbit_map_2(orbit_str: str) -> Tuple[Dict[str, Set[str]]]:
    orbit_map = {}
    orbits = orbit_str.splitlines()
    for orbit in orbits:
        parent, child = orbit.split(")")
        if not parent in orbit_map:
            orbit_map[parent] = set([])
        if not child in orbit_map:
            orbit_map[child] = set([])
        orbit_map[parent].add(child)
        orbit_map[child].add(parent)

    return orbit_map


def orbit_count(orbits: Dict[str, Set[str]]) -> int:
    total = 0
    for planet in orbits:
        total += len(_dfs(orbits, planet)) - 1
    return total


def _dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        _dfs(graph, next, visited)
    return visited


def _bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def _shortest_path(graph, start, goal):
    try:
        return next(_bfs_paths(graph, start, goal))
    except StopIteration:
        return None


def path_length(orbits):
    start = next(iter(orbits["YOU"]))
    end = next(iter(orbits["SAN"]))
    path = _shortest_path(orbits, start, end)
    return len(path) - 1  # we don't "travel" from the first planet


def main():
    with open("2019/input_day6.txt", "r") as f:
        text = f.read()
        orbits = orbit_map(text)
        print(orbit_count(orbits))
        orbits = orbit_map_2(text)
        print(path_length(orbits))


class OrbitCountTester(unittest.TestCase):
    test_input = "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L\n"

    def test1(self):
        orbits = orbit_map(self.test_input)
        count = orbit_count(orbits)
        self.assertEqual(count, 42)

    def test2(self):
        orbits = orbit_map(self.test_input + "I)SAN\nK)YOU\n")
        count = orbit_count(orbits)


if __name__ == "__main__":
    # unittest.main()
    main()
