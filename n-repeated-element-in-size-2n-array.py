from typing import List


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        found = {}
        for elem in A:
            if found.get(elem, 0) != 0:
                return elem
            found[elem] = 1
        return -1
