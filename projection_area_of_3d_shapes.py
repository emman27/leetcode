from typing import Dict, List


class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        return xy_area(grid) + xz_area(grid) + yz_area(grid)


def xy_area(grid: List[List[int]]):
    elems = []
    for row in grid:
        elems.append(list(filter(lambda height: height != 0, row)))
    return sum(map(len, elems))


def xz_area(grid: List[List[int]]):
    return sum(map(max, grid))


def yz_area(grid: List[List[int]]):
    indexes: Dict[int, List[int]] = {}
    for row in grid:
        for i, height in enumerate(row):
            if i not in indexes:
                indexes[i] = []
            indexes[i].append(height)
    return sum(map(max, indexes.values()))
