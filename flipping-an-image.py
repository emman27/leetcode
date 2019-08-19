from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [
            self.flipAndInvertRow(row) for row in A
        ]

    def flipAndInvertRow(self, row: List[int]):
        return [1 if elem == 0 else 0 for elem in reversed(row)]
