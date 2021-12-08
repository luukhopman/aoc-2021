from typing import List, Tuple


def part_one(moves: List[Tuple[str, int]]):
    horizontal, depth = 0, 0
    for d, n in moves:
        if d == 'forward':
            horizontal += n
        if d == 'down':
            depth += n
        if d == 'up':
            depth -= n
    return horizontal * depth


def part_two(moves: List[Tuple[str, int]]):
    horizontal, depth, aim = 0, 0, 0
    for d, n in moves:
        if d == 'forward':
            horizontal += n
            depth += aim * n
        if d == 'down':
            aim += n
        if d == 'up':
            aim -= n
    return horizontal * depth


if __name__ == '__main__':
    with open('input.txt') as f:
        moves = []
        for line in f:
            direction, n = line.strip().split()
            moves.append((direction, int(n)))

    print(part_one(moves))
    print(part_two(moves))
