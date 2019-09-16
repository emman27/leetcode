from typing import List


class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        top = max(A) - K
        bottom = min(A) + K
        if top < bottom:
            return 0
        else:
            return top - bottom
