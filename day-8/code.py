from typing import List, Tuple


def part_one(lines: List[Tuple[List[str], List[str]]]) -> int:
    c = 0
    for _, output in lines:
        for digit in output:
            if len(digit) in [2, 3, 4, 7]:
                c += 1
    return c


def part_two(lines: List[Tuple[List[str], List[str]]]) -> int:
    code_list = []
    for signal, output in lines:
        mapping = {}
        for digit in sorted(signal, key=len):
            if len(digit) == 2:
                mapping[1] = digit
            elif len(digit) == 3:
                mapping[7] = digit
            elif len(digit) == 4:
                mapping[4] = digit
            elif len(digit) == 5:
                if sum(1 if i in mapping[7] else 0 for i in digit) == 3:
                    mapping[3] = digit
                elif sum(1 if i in mapping[4] else 0 for i in digit) == 3:
                    mapping[5] = digit
                else:
                    mapping[2] = digit
            elif len(digit) == 6:
                if sum(1 if i in mapping[4] else 0 for i in digit) == 4:
                    mapping[9] = digit
                elif sum(1 if i in mapping[1] else 0 for i in digit) == 2:
                    mapping[0] = digit
                else:
                    mapping[6] = digit
            elif len(digit) == 7:
                mapping[8] = digit

        mapping_inv = {''.join(sorted(k)): v for v, k in mapping.items()}
        code = ''
        for digit in output:
            code += str(mapping_inv.get(''.join(sorted(digit))))
            if 'None' in code:
                break
        code_list.append(int(code))

    return sum(code_list)


if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [[x.split() for x in l.strip().split(' | ')] for l in f.readlines()]

    print(part_one(lines))
    print(part_two(lines))
