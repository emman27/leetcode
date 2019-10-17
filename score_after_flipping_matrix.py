from typing import List


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        for i, row in enumerate(A):
            if self._should_flip_row(row):
                A[i] = self._flip_row(row)
        for col in range(len(A[0])):
            if self._should_flip_col([row[col] for row in A]):
                A = self._flip_col(A, col)
        print(A)
        return self._score(A)

    def _score(self, matrix: List[List[int]]) -> int:
        return sum([int(''.join(map(str, row)), 2) for row in matrix])

    def _should_flip_row(self, row: List[int]) -> bool:
        return row[0] == 0

    def _flip_row(self, row: List[int]) -> bool:
        return [1 if item == 0 else 0 for item in row]

    def _should_flip_col(self, col: List[int]) -> bool:
        return col.count(0) > col.count(1)

    def _flip_col(self, mat: List[List[int]], col_num: int):
        for row in mat:
            row[col_num] = 1 if row[col_num] == 0 else 0
        return mat
