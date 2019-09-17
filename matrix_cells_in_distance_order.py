from typing import List


class Cell:
    def __init__(self, row: int, column: int):
        self.row = row
        self.column = column

    def distance_to(self, row: int, column: int) -> int:
        return abs(row - self.row) + abs(column - self.column)


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        cells = []
        for rowNum in range(R):
            for colNum in range(C):
                cells.append(Cell(rowNum, colNum))
        return list(map(lambda cell: [cell.row, cell.column], sorted(cells, key=lambda cell: cell.distance_to(r0, c0))))
