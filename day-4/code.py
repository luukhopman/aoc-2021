from typing import Tuple, List
import numpy as np


def part_one(numbers: List[int], boards: np.array) -> int:
    board_masks = np.zeros(boards.shape)
    for number in numbers:
        in_board = (boards == number)
        board_masks += in_board

        for board, board_mask in zip(boards, board_masks):
            if np.any(board_mask.sum(axis=1) == 5) or np.any(board_mask.sum(axis=0) == 5):
                unmarked_board = board[~board_mask.astype('bool')]
                return np.sum(unmarked_board) * number


def part_two(numbers: List[int], boards: np.array) -> int:
    board_masks = np.zeros(boards.shape)
    boards_won = []
    for number in numbers:
        in_board = (boards == number)
        board_masks += in_board

        for i, (board, board_mask) in enumerate(zip(boards, board_masks)):
            if np.any(board_mask.sum(axis=1) == 5) or np.any(board_mask.sum(axis=0) == 5):
                if i not in boards_won:
                    boards_won.append(i)
                    if len(boards_won) == 100:
                        unmarked_board = board[~board_mask.astype('bool')]
                        return np.sum(unmarked_board) * number


if __name__ == '__main__':
    with open('input.txt') as f:
        numbers, *board_list = f.read().split('\n\n')
    numbers = list(map(int, numbers.split(',')))
    board_list = [[row.split() for row in board.strip().split('\n')] for board in board_list]
    boards = np.array(board_list).astype('int')

    print(part_one(numbers, boards))
    print(part_two(numbers, boards))
