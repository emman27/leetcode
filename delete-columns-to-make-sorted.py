from typing import List


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        inverted = self._invert(A)
        count = 0
        for row in inverted:
            if sorted(row) != row:
                count += 1
        return count

    def _invert(self, A: List[str]) -> List[str]:
        mat = []
        for i in range(len(A[0])):
            mat.append(list(map(lambda s: s[i], A)))
        return mat
