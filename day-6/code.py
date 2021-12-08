from typing import List
import numpy as np


def count_lanternfish(fishes: List[int], days: int) -> int:
    fish_tracker = np.bincount(fishes, minlength=9)
    for _ in range(days):
        fish_tracker = np.roll(fish_tracker, -1)
        fish_tracker[6] += fish_tracker[8]
    return np.sum(fish_tracker)


if __name__ == '__main__':
    with open('input.txt') as f:
        fishes = [int(l.strip()) for l in f.read().split(',')]

    print(count_lanternfish(fishes, days=80))
    print(count_lanternfish(fishes, days=256))
