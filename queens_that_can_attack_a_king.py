from typing import List


def _row(piece: List[int]):
    return piece[0]


def _col(piece: List[int]):
    return piece[1]


class Solution:
    BOARD_SIZE = 8
    KING = 1
    QUEEN = 2

    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        board: List[List[int]] = []
        can: List[List[int]] = []
        for i in range(self.BOARD_SIZE):
            board.append([0]*self.BOARD_SIZE)
        board[_row(king)][_col(king)] = self.KING
        for queen in queens:
            board[_row(queen)][_col(queen)] = self.QUEEN
        to_check = []
        # right
        to_check.append(zip(
            [_row(king)] * (self.BOARD_SIZE-_col(king)),
            range(_col(king), self.BOARD_SIZE)
        ))
        # down
        to_check.append(zip(
            range(_row(king), self.BOARD_SIZE),
            [_col(king)] * (self.BOARD_SIZE-_row(king))
        ))
        # up
        to_check.append(zip(
            range(_row(king), -1, -1),
            [_col(king)] * (_row(king)+1)
        ))
        # left
        to_check.append(zip(
            [_row(king)] * (_col(king)+1),
            range(_col(king), -1, -1)
        ))
        # southeast
        to_check.append(zip(
            range(_row(king), self.BOARD_SIZE),
            range(_col(king), self.BOARD_SIZE)
        ))
        # southwest
        to_check.append(zip(
            range(_row(king), self.BOARD_SIZE),
            range(_col(king), -1, -1)
        ))
        # northeast
        to_check.append(zip(
            range(_row(king), -1, -1),
            range(_col(king), self.BOARD_SIZE)
        ))
        # northwest
        to_check.append(zip(
            range(_row(king), -1, -1),
            range(_col(king), -1, -1)
        ))
        for checkable in to_check:
            ret = self._check_range(board, checkable)
            if ret:
                can.append(ret)
        return can

    def _check_range(self, board, coordinate_range):
        for row, col in coordinate_range:
            if board[row][col] == self.QUEEN:
                return [row, col]
        return None
