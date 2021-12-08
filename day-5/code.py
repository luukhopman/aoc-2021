import numpy as np


def part_one(coordinates: list) -> int:
    a = np.zeros((1000, 1000))
    for (x1, y1), (x2, y2) in coordinates:
        if (x1 == x2) or (y1 == y2):
            for x in range(min(x1, x2), max(x1, x2)+1):
                for y in range(min(y1, y2), max(y1, y2)+1):
                    a[y, x] += 1
    return np.sum(a >= 2)


def part_two(coordinates: list) -> int:
    a = np.zeros((1000, 1000))
    for (x1, y1), (x2, y2) in coordinates:
        if (x1 == x2) or (y1 == y2):
            for x in range(min(x1, x2), max(x1, x2)+1):
                for y in range(min(y1, y2), max(y1, y2)+1):
                    a[y, x] += 1
        elif abs(x2-x1) == abs(y2-y1):
            dist = abs(x2-x1)
            for i in range(dist+1):
                if (x1 > x2) and (y1 > y2):
                    a[y1-i, x1-i] += 1
                elif (x1 < x2) and (y1 > y2):
                    a[y1-i, x1+i] += 1
                elif (x1 > x2) and (y1 < y2):
                    a[y1+i, x1-i] += 1
                elif (x1 < x2) and (y1 < y2):
                    a[y1+i, x1+i] += 1
    return np.sum(a >= 2)


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [l.split('->') for l in f.readlines()]
        coordinates = [[tuple(map(int, a.split(','))), tuple(map(int, b.split(',')))] for a, b in lines]

    print(part_one(coordinates))
    print(part_two(coordinates))
