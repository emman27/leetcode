from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(map(lambda elem: elem ** 2, A))
