from typing import List


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        indexes = []
        for (idx, char) in enumerate(S):
            if char == C:
                indexes.append(idx)
        result = []
        for i in range(len(S)):
            result.append(min(list(map(lambda index_of_c: abs(index_of_c - i), indexes))))
        return result
