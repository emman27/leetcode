from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        return list(range(1, label+1))
