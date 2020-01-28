from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diagonals = []
        for row in range(len(mat)):
            diagonal = []
            for i in range(min(len(mat)-row, len(mat[0]))):
                diagonal.append(mat[i+row][i])
            diagonals.append(diagonal)
        for col in range(1, len(mat[0])):
            diagonal = []
            for i in range(min(len(mat), len(mat[0])-col)):
                diagonal.append(mat[i][i+col])
            diagonals.append(diagonal)
        for diagonal in diagonals:
            diagonal.sort()
        ans = []
        for row in mat:
            ans.append([0]*len(mat[0]))

        index = 0
        for row in range(len(mat)):
            for i in range(min(len(mat)-row, len(mat[0]))):
                ans[i+row][i] = diagonals[index][i]
            index += 1
        for col in range(1, len(mat[0])):
            for i in range(min(len(mat), len(mat[0])-col)):
                ans[i][i+col] = diagonals[index][i]
            index += 1
        return ans
