from typing import List


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        for i, row in enumerate(A):
            if self._should_flip(row):
                A[i] = self._flip(row)
        return self._score(A)

    def _score(self, matrix: List[List[int]]) -> int:
        return sum([int(''.join(map(str, row)), 2) for row in matrix])

    def _should_flip(self, row: List[int]) -> bool:
        return row[0] == 0

    def _flip(self, row: List[int]) -> bool:
        return [1 if item == 0 else 0 for item in row]
