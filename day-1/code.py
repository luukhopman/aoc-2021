from typing import List


def part_one(data: List[int]) -> int:
    return sum(data[i-1] < d for i, d in enumerate(data) if i > 0)


def part_two(data: List[int]) -> int:
    return sum(sum(data[i:i+3]) > sum(data[i-1:i-1+3]) for i, _ in enumerate(data) if i > 0)


if __name__ == '__main__':
    with open('input.txt') as f:
        depth_list = [int(i) for i in f.readlines()]

    print(part_one(depth_list))
    print(part_two(depth_list))
