from typing import List


class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        even = len([chip for chip in chips if chip % 2 == 0])
        return min(even, len(chips) - even)
