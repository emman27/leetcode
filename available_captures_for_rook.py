from typing import Iterator, List, Tuple

DIRECTIONS = ['U', 'D', 'L', 'R']


def get_rook_position(board: List[List[str]]) -> Tuple[int, int]:
    for rowNum, row in enumerate(board):
        for colNum, piece in enumerate(row):
            if piece == 'R':
                return (rowNum, colNum)
    return (-1, -1)


def pieces_in_path(board: List[List[str]], rook_position: Tuple[int, int], direction: str) -> List[str]:
    row, col = rook_position
    if direction == 'R':
        return board[row][col+1:]
    elif direction == 'L':
        return list(reversed(board[row][:col]))
    column = list(map(lambda row: row[col], board))
    if direction == 'D':
        return column[row + 1:]
    elif direction == 'U':
        return list(reversed(column[:row]))
    return []


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook_position = get_rook_position(board)
        edible_pawns = 0
        for direction in DIRECTIONS:
            path = pieces_in_path(board, rook_position, direction)
            for piece in path:
                if piece == 'B':
                    break
                if piece == 'p':
                    edible_pawns += 1
                    break
        return edible_pawns
