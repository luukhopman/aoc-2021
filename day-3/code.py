from typing import List


def part_one(binary: List[str]) -> int:
    gamma, epsilon = '', ''
    for i in range(len(binary[0])):
        zero_count, one_count = 0, 0
        for j in binary:
            if j[i] == '0':
                zero_count += 1
            if j[i] == '1':
                one_count += 1
        if zero_count > one_count:
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    return int(gamma, 2) * int(epsilon, 2)


def part_two(binary: List[str]) -> int:
    oxygen = binary
    for i in range(len(oxygen[0])):
        zero_count, one_count = 0, 0
        for j in oxygen:
            if j[i] == '0':
                zero_count += 1
            if j[i] == '1':
                one_count += 1
        if zero_count > one_count:
            oxygen = [x for x in oxygen if x[i] == '0']
        else:
            oxygen = [x for x in oxygen if x[i] == '1']
        if len(oxygen) == 1:
            break

    scrubber = binary
    for i in range(len(scrubber[0])):
        zero_count, one_count = 0, 0
        for j in scrubber:
            if j[i] == '0':
                zero_count += 1
            if j[i] == '1':
                one_count += 1
        if zero_count > one_count:
            scrubber = [x for x in scrubber if x[i] == '1']
        else:
            scrubber = [x for x in scrubber if x[i] == '0']
        if len(scrubber) == 1:
            break

    return int(oxygen[0], 2) * int(scrubber[0], 2)


if __name__ == '__main__':
    with open('input.txt') as f:
        binary = [i.strip() for i in f.readlines()]

    print(part_one(binary))
    print(part_two(binary))
