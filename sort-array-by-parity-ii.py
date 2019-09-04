from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = filter(lambda x: x % 2 == 1, A)
        even = filter(lambda x: x % 2 == 0, A)
        result = []
        for e, o in zip(even, odd):
            result.extend([e, o])
        return result
