from typing import List
import numpy as np


def part_one(crab_positions: List[int]) -> int:
    fuel_min = None
    for pos in range(max(crab_positions)):
        fuel = np.sum(np.abs(crab_positions-pos))
        if not fuel_min:
            fuel_min = fuel
        elif fuel < fuel_min:
            fuel_min = fuel
    return fuel_min


def part_two(crab_positions: List[int]) -> int:
    fuel_min = None
    fuel_costs = np.arange(1, max(crab_positions))
    for pos in range(max(crab_positions)):
        steps = np.abs(crab_positions-pos)
        fuel = 0
        for step in steps:
            fuel += np.sum(fuel_costs[0:step])
        if not fuel_min:
            fuel_min = fuel
        elif fuel < fuel_min:
            fuel_min = fuel
    return fuel_min


if __name__ == '__main__':
    with open('input.txt') as f:
        crab_positions = np.array([int(l.strip()) for l in f.read().split(',')])

    print(part_one(crab_positions))
    print(part_two(crab_positions))
