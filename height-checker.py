from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_heights = sorted(heights)
        count = 0
        for left, right in zip(sorted_heights, heights):
            if left != right:
                count += 1
        return count
