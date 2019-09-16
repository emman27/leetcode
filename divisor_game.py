class Solution:
    def divisorGame(self, N: int) -> bool:
        if N == 1:
            return False
        elif N == 2:
            return True
        else:
            return not self.divisorGame(N-1)
