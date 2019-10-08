from typing import List


class Coordinate:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col

    def __repr__(self):
        return f'({self.row}, {self.col})'


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        squares_covered = sum(map(lambda row: row.count(0), grid))
        possible_paths: List[List[Coordinate]] = [[self._start_coordinates(grid)]]
        print(possible_paths)
        paths: List[List[Coordinate]] = []
        while possible_paths:
            path = possible_paths.pop()
            for coordinate in self._generate_next_coordinate(grid, path):
                new_path = path+[coordinate]
                if grid[coordinate.row][coordinate.col] == 2:
                    paths.append(new_path)
                else:
                    possible_paths.append(new_path)
        return len(list(filter(lambda path: len(path) == squares_covered + 2, paths)))

    def _start_coordinates(self, grid: List[List[int]]) -> Coordinate:
        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if col == 1:
                    return Coordinate(r, c)
        raise Exception("Cannot find starting coordinate")

    def _generate_next_coordinate(self, grid: List[List[int]], path: List[Coordinate]) -> List[Coordinate]:
        last_coordinate = path[-1]
        possible = filter(
            lambda coord: coord not in path,
            filter(
                lambda coord: grid[coord.row][coord.col] != -1,
                filter(
                    lambda coord: coord.col >= 0 and coord.col < len(grid[0]),
                    filter(
                        lambda coord: coord.row >= 0 and coord.row < len(grid), [
                            Coordinate(last_coordinate.row+1, last_coordinate.col),
                            Coordinate(last_coordinate.row-1, last_coordinate.col),
                            Coordinate(last_coordinate.row, last_coordinate.col + 1),
                            Coordinate(last_coordinate.row, last_coordinate.col - 1),
                        ]
                    )
                )
            )
        )
        return list(possible)
