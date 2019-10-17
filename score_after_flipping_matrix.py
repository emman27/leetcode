from typing import List


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        return self._score(A)

    def _score(self, matrix: List[List[int]]) -> int:
        return sum([int(''.join(map(str, row)), 2) for row in matrix])
