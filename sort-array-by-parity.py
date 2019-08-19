class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return [elem for elem in A if elem % 2 == 0] + [elem for elem in A if elem % 2 == 1]
