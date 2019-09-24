from typing import List


def max_height_in_row(grid: List[List[int]], row: int) -> int:
    return max(grid[row])


def max_height_in_col(grid: List[List[int]], col: int) -> int:
    return max(map(lambda row: row[col], grid))


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        total_increase = 0
        for row_num, row in enumerate(grid):
            for col_num, height in enumerate(row):
                total_increase += min(max_height_in_row(grid, row_num), max_height_in_col(grid, col_num)) - height
        return total_increase
