from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        cache = self._generate_cache(mat)
        ans = []
        for row in cache:
            ans.append([0]*len(row))
        for (i, row) in enumerate(cache):
            for (j, col) in enumerate(row):
                ans[i][j] = (
                    self._get(cache, i+K, j+K) +
                    self._get(cache, i-K-1, j-K-1) -
                    self._get(cache, i+K, j-K-1) -
                    self._get(cache, i-K-1, j+K)
                )
        return ans

    def _generate_cache(self, mat: List[List[int]]) -> List[List[int]]:
        cache = []
        for row in mat:
            cache.append([0]*len(row))
        for (i, row) in enumerate(mat):
            for (j, col) in enumerate(row):
                cache[i][j] = mat[i][j] + self._get(cache, i-1, j) + self._get(cache, i, j-1) - self._get(cache, i-1, j-1)
        return cache

    def _get(self, mat: List[List[int]], row: int, col: int):
        if row < 0 or col < 0:
            return 0
        row = min(len(mat)-1, row)
        col = min(len(mat[0])-1, col)
        return mat[row][col]
